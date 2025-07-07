# 🎬 Smart-Movie-Recommender 🎥

This AI-powered project delivers personalized movie suggestions using **content-based filtering** and an interactive **Streamlit UI**. It recommends movies based on the similarity of features like genres, keywords, cast, and overview using cosine similarity techniques.

---

## 🌟 Project Preview

> ✅ Built with Streamlit for a seamless user experience  
> 🧠 AI-powered, content-based movie recommendations  
> 🖼️ Posters and metadata fetched dynamically using the TMDB API  
> 🎞️ Explore top 6 similar movies with trailers and metadata  

(![image](https://github.com/user-attachments/assets/8fd023f3-6437-4683-9c59-573a3e757b45)

---

## 🔍 Problem Statement

With thousands of movies released every year, it becomes overwhelming for users to decide **what to watch next**.

> ### ❓ “Can we build an intelligent system that recommends similar movies based on a user’s interest?”

---

## 🎯 Objectives

- Develop a movie recommendation engine using **content-based filtering**
- Apply **cosine similarity** on transformed movie feature vectors
- Fetch **real-time movie posters, genres, and trailers** using the **TMDB API**
- Build an interactive **Streamlit web app** for dynamic user experience

---

## 🗂️ Project Structure

| File Name            | Description                                    |
|----------------------|------------------------------------------------|
| `app.py`             | Main Streamlit web application                 |
| `Main_File.ipynb`    | Model building and feature vectorization       |
| `movie_list.pkl`     | Preprocessed movie metadata                    |
| `similarity.pkl.gz`  | Compressed cosine similarity matrix            |
| `requirements.txt`   | Required Python dependencies                   |
| `README.md`          | Project documentation                          |

---

## 🧠 Features

- 🔎 Intelligent movie search via dropdown
- 🎥 Embedded YouTube trailer for each movie
- 🧠 AI-powered recommendations based on cosine similarity
- 🖼️ Real-time poster and genre info using TMDB API
- 🎛️ Clean 2x3 horizontal layout for results

---

## 🛠️ Tools & Technologies

- **Python 3.8+**
- **Pandas** – Data preprocessing and manipulation  
- **Scikit-learn** – Vectorization and similarity calculations  
- **Pickle + GZip** – Serialization and compression  
- **Streamlit** – Frontend web UI  
- **TMDB API** – Movie metadata and posters  
- **Requests** – API handling  

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Smart-Movie-Recommender.git
cd Smart-Movie-Recommender
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
streamlit run app.py
```
---

## 📈 Key Learnings

- ✅ Practical understanding of **content-based filtering**
- 🔍 Application of **cosine similarity** in real-world scenarios
- 🧠 Feature vector engineering for **text-based movie metadata**
- 🖥️ Responsive and dynamic UI building using **Streamlit**
- 🌐 Real-time **integration with external APIs** (TMDB)

---

## 📌 Future Enhancements

- 🧠 Add **collaborative filtering** for user-based recommendations
- 🎭 Add filters by **genre**, **cast**, and **release year**
- 📊 Integrate **IMDb** and **RottenTomatoes** ratings & vote counts
- 🗂️ Implement **watchlist functionality** for registered users
- 💬 Capture **user feedback** and train feedback-aware recommendation models

---

## 📬 Connect with Me

- 💼 [LinkedIn – Manthan Jadav](https://www.linkedin.com/in/manthanjadav/)
- 📧 [manthanjadav746@gmail.com](mailto:manthanjadav746@gmail.com)

---

## ❤️ Made with passion for movie lovers!

