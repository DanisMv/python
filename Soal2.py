# Data for each book
books = [
    {"kode_buku": "AF003", "judul": "Bahasa Inggris", "penerbit": "Erlangga", "jumlah": 12, "harga_beli": 15000},
    {"kode_buku": "QS005", "judul": "Kepemimpinan", "penerbit": "Elex ME", "jumlah": 10, "harga_beli": 10000}
]

# Function to calculate total and apply conditions
def calculate_book_totals(books):
    for book in books:
        # Calculate total price
        total = book["jumlah"] * book["harga_beli"]
        book["total"] = total
        
        # Apply voucher if more than 12 books
        if book["jumlah"] > 12:
            book["voucher"] = "Yes"
            # Assuming a discount of 10% for demonstration
            book["diskon"] = 0.1 * total
        else:
            book["voucher"] = "No"
            book["diskon"] = 0  # No discount if less than 12 books
    
    return books

# Calculate and display results
book_totals = calculate_book_totals(books)

for book in book_totals:
    print(f"Kode Buku: {book['kode_buku']}")
    print(f"Judul: {book['judul']}")
    print(f"Penerbit: {book['penerbit']}")
    print(f"Jumlah: {book['jumlah']}")
    print(f"Harga Beli: {book['harga_beli']}")
    print(f"Total Harga: {book['total']}")
    print(f"Voucher: {book['voucher']}")
    print(f"Diskon: {book['diskon']}")
    print("-" * 30)
