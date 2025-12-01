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

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        // Show popup with loading state
        showPopup();
        showLoading();

        // Get form data
        const formData = new FormData(form);

        try {
            // Submit form to the detect API endpoint
            const response = await fetch("/detect", {
                method: "POST",
                body: formData
            });

            const data = await response.json();
            
            console.log("API Response:", data); // Debug log

            // Simulate minimum loading time for better UX
            setTimeout(() => {
                if (data.success) {
                    showResult(data.result, data.is_phishing);
                } else {
                    showResult("Error", false);
                }
            }, 1500);

        } catch (error) {
            console.error("Error:", error);
            setTimeout(() => {
                showResult("Error", false);
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

function showResult(result, isPhishing) {
    const loadingState = document.getElementById("loadingState");
    const resultState = document.getElementById("resultState");
    const resultIcon = document.getElementById("resultIcon");
    const resultText = document.getElementById("resultText");
    const resultDescription = document.getElementById("resultDescription");

    // Hide loading, show result
    loadingState.classList.add("hidden");
    resultState.classList.remove("hidden");

    console.log("Showing result:", result, "Is Phishing:", isPhishing); // Debug log

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