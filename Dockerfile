# Kita pakai Python versi ringan (Alpine Linux)
FROM python:3.9-alpine

WORKDIR /app

# Copy daftar belanjaan library dulu
COPY requirements.txt .
# Install library di dalam container
RUN pip install --no-cache-dir -r requirements.txt

# PENTING: Install CURL.
# Ini wajib ada karena nanti kita pakai command 'curl' untuk ngecek kesehatan aplikasi
RUN apk --no-cache add curl

# Copy sisa kode aplikasi
COPY . .

# Buka jalur port 5000
EXPOSE 5000

# Perintah untuk menjalankan aplikasi
CMD ["python", "app.py"]