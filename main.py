import os

from src.chunking import chunk_text
from src.conflict_resolver import resolve_conflicts
from src.ddr_generator import generate_ddr
from src.extract import extract_pdf_data
from src.image_analyzer import analyze_images
from src.pdf_generator import generate_pdf
from src.structured_extractor import extract_structured


def run_pipeline(inspect_path, thermal_path):
    os.makedirs("extracted/images", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    inspection_pages, _ = extract_pdf_data(
        inspect_path,
        "extracted/images",
        source_name="inspection",
    )
    thermal_pages, _ = extract_pdf_data(
        thermal_path,
        "extracted/images",
        source_name="thermal",
    )

    image_pages = analyze_images(inspection_pages + thermal_pages)
    # ✅ SAFETY HANDLING (PUT HERE)
    if isinstance(image_pages, str):
        image_pages = [image_pages]

    chunks = chunk_text(inspection_pages + thermal_pages + [image_pages])
    structured = extract_structured(chunks)
    if not isinstance(structured, list):
        structured = [structured]
    resolved = resolve_conflicts(structured)
    report = generate_ddr(resolved)

    generate_pdf(report, "output/final_ddr.pdf")
    return report


if __name__ == "__main__":
    run_pipeline("data/inspection_report.pdf", "data/thermal_report.pdf")
print("\n✅ DDR GENERATED SUCCESSFULLY\n")