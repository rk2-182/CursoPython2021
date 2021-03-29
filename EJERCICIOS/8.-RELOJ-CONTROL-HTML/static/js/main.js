const btnDelete= document.querySelectorAll('.btn-eliminar');
if(btnDelete) {
  const btnArray = Array.from(btnDelete);
  btnArray.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      if(!confirm('Esta seguro que desea eliminar?')){
        e.preventDefault();
      }
    });
  })
}