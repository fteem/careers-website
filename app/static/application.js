const toastTrigger = document.getElementById('liveToastBtn')
const toastLiveExample = document.getElementById('liveToast')
const toastBody = document.getElementById('toast-body')
const loadingSpinner = document.getElementById('loadingSpinner')

if (toastTrigger) {
  const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
  toastTrigger.addEventListener('click', async () => {
    loadingSpinner.removeAttribute("hidden");
    let slug = event.target.getAttribute('data-slug');
    fetch("/summarize/" + slug)
      .then((response) => response.text())
      .then((data) => {
        toastBody.innerHTML = data
        toastBootstrap.show()
        loadingSpinner.setAttribute("hidden", "true");
      })
  })
}
