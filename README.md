# Ôn tập CCNA

Web tĩnh ôn tập ~795 câu hỏi CCNA: ôn theo từng phần, ôn ngẫu nhiên, ôn lại câu sai, dịch Anh → Việt (Google Translate, có cache).

- `web/` — trang web (mở `web/index.html` là chạy).
- `tools/extract.py` — trích xuất câu hỏi từ các file `.docx` sang `web/data.js` + `web/img/` (cần `pip install python-docx`).

Deploy Vercel: import repo, không cần build — `vercel.json` đặt `outputDirectory` là `web`.
