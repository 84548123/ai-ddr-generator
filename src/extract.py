import os
import re

import fitz


def _normalize_text(text):
    text = text or ""
    text = text.replace("\x00", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_pdf_data(pdf_path, image_output, source_name):
    doc = fitz.open(pdf_path)
    pages = []
    images = []

    source_image_dir = os.path.join(image_output, source_name)
    os.makedirs(source_image_dir, exist_ok=True)

    for page_num, page in enumerate(doc, start=1):
        page_text = _normalize_text(page.get_text())
        page_images = []

        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            img_path = os.path.join(
                source_image_dir,
                f"img_p{page_num}_{img_index}.png",
            )

            with open(img_path, "wb") as file_obj:
                file_obj.write(image_bytes)

            page_images.append(img_path)
            images.append(img_path)

        pages.append(
            {
                "source": source_name,
                "page": page_num,
                "text": page_text,
                "images": page_images,
            }
        )

    doc.close()
    return pages, images
