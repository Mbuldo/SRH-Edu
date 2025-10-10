// api.js
const BASE_URL = 'http://localhost:8000/api';

const api = {
    // STI Information
    async getSTIInfo() {
        const response = await fetch(`${BASE_URL}/content/`);
        return await response.json();
    },

    // Quiz
    async getQuizQuestions() {
        const response = await fetch(`${BASE_URL}/quiz/questions`);
        return await response.json();
    },

    async submitQuiz(answers) {
        const response = await fetch(`${BASE_URL}/quiz/submit`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(answers),
        });
        return await response.json();
    },

    // Clinics
    async getClinics(area = '') {
        const response = await fetch(`${BASE_URL}/clinics/?area=${area}`);
        return await response.json();
    },

    // Symptoms
    async checkSymptoms(symptoms) {
        const response = await fetch(`${BASE_URL}/symptoms/check`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(symptoms),
        });
        return await response.json();
    },

    // Admin Authentication
    async login(username, password) {
        const formData = new FormData();
        formData.append('username', username);
        formData.append('password', password);

        const response = await fetch(`${BASE_URL}/auth/login`, {
            method: 'POST',
            body: formData,
        });
        return await response.json();
    }
};

export default api;
