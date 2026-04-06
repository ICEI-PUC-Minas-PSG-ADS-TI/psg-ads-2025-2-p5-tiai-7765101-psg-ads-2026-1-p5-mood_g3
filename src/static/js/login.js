function switchTab(tab) {
    const formLogin = document.getElementById('form-login');
    const formCadastro = document.getElementById('form-cadastro');
    const btnLogin = document.getElementById('btn-login');
    const btnCadastro = document.getElementById('btn-cadastro');

    if (tab === 'login') {
        formLogin.style.display = 'block';
        formCadastro.style.display = 'none';
        btnLogin.classList.add('active');
        btnCadastro.classList.remove('active');
    } else {
        formLogin.style.display = 'none';
        formCadastro.style.display = 'block';
        btnCadastro.classList.add('active');
        btnLogin.classList.remove('active');
    }
}

