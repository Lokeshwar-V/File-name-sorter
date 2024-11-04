import os

def sort_files(folder_path):
    files = os.listdir(folder_path)
    files.sort()  
    return files

if __name__ == "__main__":
    folder_path = "G:\\4-Lokeshwar\\Images\\2024"  
    sorted_files = sort_files(folder_path)
    print("Sorted files:", sorted_files)
    
    