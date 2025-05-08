window.addEventListener("load", () => {
  // Add toggle listener to all elements with .collapse-toggle
  const toggleButtons = document.querySelectorAll("details");

  // Handle game filter input
  const gameSearch = document.getElementById("game-search");
  gameSearch.value = "";
  gameSearch.addEventListener("input", (evt) => {
    if (!evt.target.value.trim()) {
      // If input is empty, display all games as collapsed
      return toggleButtons.forEach((header) => {
        header.style.display = null;
        header.removeAttribute("open");
      });
    }

    // Loop over all the games
    toggleButtons.forEach((header) => {
      // If the game name includes the search string, display the game. If not, hide it
      if (
        header
          .getAttribute("data-game")
          .toLowerCase()
          .includes(evt.target.value.toLowerCase()) ||
        header
          .getAttribute("data-display-name")
          .toLowerCase()
          .includes(evt.target.value.toLowerCase())
      ) {
        header.style.display = null;
        header.setAttribute("open", "1");
      } else {
        header.style.display = "none";
        header.removeAttribute("open");
      }
    });
  });

  document.getElementById("expand-all").addEventListener("click", expandAll);
  document
    .getElementById("collapse-all")
    .addEventListener("click", collapseAll);

  const COOKIE_NAME = "show_hidden_games";

  function setCookie(name, value, days = 365) {
    const expires = new Date(
      Date.now() + days * 24 * 60 * 60 * 1000
    ).toUTCString();
    document.cookie = `${name}=${value};expires=${expires};path=/`;
  }

  function getCookie(name) {
    return document.cookie
      .split("; ")
      .find((row) => row.startsWith(name + "="))
      ?.split("=")[1];
  }

  function updateNSFWVisibility() {
    const show = getCookie(COOKIE_NAME) === "true";
    document.querySelectorAll('details[data-nsfw="true"]').forEach((el) => {
      el.style.display = show ? "" : "none";
    });
    document.getElementById("toggle-nsfw").textContent = show
      ? "Hide NSFW games"
      : "Show NSFW games";
  }

  document.getElementById("toggle-nsfw").addEventListener("click", (e) => {
    e.preventDefault();
    const currently = getCookie(COOKIE_NAME) === "true";
    setCookie(COOKIE_NAME, !currently);
    updateNSFWVisibility();
  });

  updateNSFWVisibility();
});

const expandAll = () => {
  document.querySelectorAll("details").forEach((detail) => {
    detail.setAttribute("open", "1");
  });
};

const collapseAll = () => {
  document.querySelectorAll("details").forEach((detail) => {
    detail.removeAttribute("open");
  });
};
