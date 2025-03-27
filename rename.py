import os

def rename_pdf_files(base_path):
    # Iterate over all items in the base directory
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        
        # Process only directories
        if os.path.isdir(item_path):
            # Extract the part before the first underscore
            name_lastname_part = item.split("_")[0].strip()

            # Replace spaces with underscores to get the desired filename
            name_lastname = name_lastname_part.replace(" ", "_")
            new_pdf_name = f"{name_lastname}.pdf"

            # Look for PDF files inside the directory
            pdf_files = [f for f in os.listdir(item_path) if f.lower().endswith('.pdf')]

            if pdf_files:
                old_pdf_path = os.path.join(item_path, pdf_files[0])  # Assuming there's only one PDF
                new_pdf_path = os.path.join(item_path, new_pdf_name)

                # Rename the PDF file
                try:
                    os.rename(old_pdf_path, new_pdf_path)
                    print(f"Renamed: {old_pdf_path} -> {new_pdf_path}")
                except Exception as e:
                    print(f"Failed to rename {old_pdf_path}: {e}")
            else:
                print(f"No PDF found in: {item_path}")

if __name__ == "__main__":
    base_directory = os.path.dirname(os.path.abspath(__file__))  # Current script directory
    rename_pdf_files(base_directory)
