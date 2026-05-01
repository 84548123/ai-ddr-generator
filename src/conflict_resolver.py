def _normalized_key(item):
    return (
        item.get("area", "").strip().lower(),
        item.get("issue", "").strip().lower(),
    )


def resolve_conflicts(data):
    grouped = {}

    for item in data:
        key = _normalized_key(item)
        grouped.setdefault(key, []).append(item)

    resolved = []
    severity_rank = {"Unknown": 0, "Low": 1, "Medium": 2, "High": 3}

    for items in grouped.values():
        merged = dict(items[0])
        merged["source_pages"] = []
        merged["missing_information"] = []
        merged["conflict"] = None

        severities = set()
        observations = set()
        evidence_parts = []

        for item in items:
            severity = item.get("severity", "Unknown")
            severities.add(severity)
            observations.add(item.get("thermal_observation", ""))
            evidence = item.get("evidence", "")
            if evidence and evidence not in evidence_parts:
                evidence_parts.append(evidence)

            for source_page in item.get("source_pages", []):
                if source_page not in merged["source_pages"]:
                    merged["source_pages"].append(source_page)

            for missing in item.get("missing_information", []):
                if missing not in merged["missing_information"]:
                    merged["missing_information"].append(missing)

            if severity_rank.get(severity, 0) > severity_rank.get(merged.get("severity", "Unknown"), 0):
                merged["severity"] = severity

            if (
                item.get("inspection_observation")
                and item["inspection_observation"] != "Not Available"
            ):
                merged["inspection_observation"] = item["inspection_observation"]

            if (
                item.get("thermal_observation")
                and item["thermal_observation"] != "Not Available"
            ):
                merged["thermal_observation"] = item["thermal_observation"]

        merged["evidence"] = " | ".join(evidence_parts) if evidence_parts else "Not Available"

        if len(severities) > 1:
            merged["conflict"] = "Sources imply different severity levels for the same issue."
        elif len(observations) > 1 and "Not Available" not in observations:
            merged["conflict"] = "Sources describe this issue differently."

        resolved.append(merged)

    resolved.sort(
        key=lambda item: (
            -severity_rank.get(item.get("severity", "Unknown"), 0),
            item.get("area", ""),
            item.get("issue", ""),
        )
    )
    return resolved
