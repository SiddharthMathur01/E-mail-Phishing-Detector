document.addEventListener("DOMContentLoaded", () => {
    const card = document.querySelector(".card");
    const content = card.querySelector(".card-content");
    const isTouchDevice = "ontouchstart" in window || navigator.maxTouchPoints > 0;
    const rotationFactor = 2;

    // Card 3D tilt effect
    if (!isTouchDevice) {
        card.addEventListener("mousemove", (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const rotateY = (rotationFactor * (x - centerX)) / centerX;
            const rotateX = (-rotationFactor * (y - centerY)) / centerY;

            content.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
            card.style.setProperty("--x", `${(x / rect.width) * 100}%`);
            card.style.setProperty("--y", `${(y / rect.height) * 100}%`);
        });

        card.addEventListener("mouseleave", () => {
            content.style.transform = "rotateX(0) rotateY(0)";
            content.style.transition = "transform 0.5s ease";
            setTimeout(() => {
                content.style.transition = "";
            }, 500);
        });
    }

    // Form submission handling
    const form = document.getElementById("phishingForm");
    const popupOverlay = document.getElementById("popupOverlay");
    const loadingState = document.getElementById("loadingState");
    const resultState = document.getElementById("resultState");
    const resultIcon = document.getElementById("resultIcon");
    const resultText = document.getElementById("resultText");
    const resultDescription = document.getElementById("resultDescription");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        // Show popup with loading state
        showPopup();
        showLoading();

        // Get form data
        const formData = new FormData(form);

        try {
            // Submit form to server
            const response = await fetch("/", {
                method: "POST",
                body: formData
            });

            const html = await response.text();
            
            // Parse the response to extract the result
            // The server should return the result in a specific format
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, "text/html");
            const resultElement = doc.querySelector("#detectionResult");
            
            let result = "Safe Email"; // default
            if (resultElement) {
                result = resultElement.textContent.trim();
            }

            // Simulate minimum loading time for better UX
            setTimeout(() => {
                showResult(result);
            }, 1500);

        } catch (error) {
            console.error("Error:", error);
            setTimeout(() => {
                showResult("Error");
            }, 1500);
        }
    });
});

function showPopup() {
    const popupOverlay = document.getElementById("popupOverlay");
    popupOverlay.classList.add("active");
}

function showLoading() {
    const loadingState = document.getElementById("loadingState");
    const resultState = document.getElementById("resultState");
    
    loadingState.classList.remove("hidden");
    resultState.classList.add("hidden");
}

function showResult(result) {
    const loadingState = document.getElementById("loadingState");
    const resultState = document.getElementById("resultState");
    const resultIcon = document.getElementById("resultIcon");
    const resultText = document.getElementById("resultText");
    const resultDescription = document.getElementById("resultDescription");

    // Hide loading, show result
    loadingState.classList.add("hidden");
    resultState.classList.remove("hidden");

    // Determine if phishing or safe
    const isPhishing = result.toLowerCase().includes("phishing email");

    if (isPhishing) {
        resultIcon.className = "result-icon phishing";
        resultText.className = "result-text phishing";
        resultText.textContent = "Phishing Email";
        resultDescription.textContent = "This email appears to be a phishing attempt. Be cautious!";
    } else {
        resultIcon.className = "result-icon safe";
        resultText.className = "result-text safe";
        resultText.textContent = "Safe Email";
        resultDescription.textContent = "This email appears to be legitimate and safe.";
    }
}

function closePopup() {
    const popupOverlay = document.getElementById("popupOverlay");
    popupOverlay.classList.remove("active");
}

// Close popup when clicking outside
document.addEventListener("click", (e) => {
    const popupOverlay = document.getElementById("popupOverlay");
    if (e.target === popupOverlay) {
        closePopup();
    }
});