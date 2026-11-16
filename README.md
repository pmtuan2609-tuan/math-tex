# MathTex Pro Web 2026

Ứng dụng Web Soạn Đề & Đảo Đề Thi Trắc Nghiệm GDPT 2018 Xuất File Word (.docx) chạy trên **Vercel Serverless (Python FastAPI + HTML/Tailwind)**.

## Cấu trúc thư mục

```text
MathTex_Web_Vercel/
├── api/
│   └── index.py         # Backend Python FastAPI (Sinh đề, Đảo đề, python-docx xuất Word)
├── public/
│   └── index.html       # Giao diện Web hiện đại, MathJax hiển thị công thức Toán
├── requirements.txt     # Danh sách thư viện Python tự động cài đặt trên Vercel
├── vercel.json          # Cấu hình định tuyến Serverless Vercel
└── README.md
```

## Cách triển khai lên GitHub & Vercel (3 phút)

### Bước 1: Đưa lên GitHub
1. Mở [GitHub.com](https://github.com), tạo 1 repository mới (ví dụ: `mathtex-web`).
2. Dùng GitHub Desktop (hoặc Git CLI / tải trực tiếp) để đẩy toàn bộ các file trong thư mục này lên repository đó.

### Bước 2: Liên kết với Vercel
1. Đăng nhập [Vercel.com](https://vercel.com) (chọn **Continue with GitHub**).
2. Bấm **Add New...** -> **Project**.
3. Chọn repository `mathtex-web` vừa tạo và bấm **Import**.
4. Giữ nguyên các thông số mặc định và bấm nút **Deploy**.

Sau 1 phút, Vercel sẽ cấp cho bạn một đường link miễn phí dạng `https://mathtex-web.vercel.app` để sử dụng ngay trên mọi thiết bị!
