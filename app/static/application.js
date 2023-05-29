const toastTrigger = document.getElementById('liveToastBtn')
const toastLiveExample = document.getElementById('liveToast')
const toastBody = document.getElementById('toast-body')

if (toastTrigger) {
  const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
  console.log(toastBootstrap);
  toastTrigger.addEventListener('click', async () => {
    let slug = event.target.getAttribute('data-slug');
    fetch("/summarize/" + slug)
      .then((response) => response.text())
      .then((data) => {
        toastBody.innerHTML = data
        toastBootstrap.show()
      })
  })
}
