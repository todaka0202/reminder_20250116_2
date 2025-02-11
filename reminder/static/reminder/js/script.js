const buttons = document.querySelectorAll(".not_implemented").forEach((editButton) => {
    editButton.addEventListener("click", () => {
        alert("この機能は実装されていません")
    });
});