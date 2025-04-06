/*Link do linkedin */

const linkedinLink = document.querySelector('footer a');

linkedinLink.onmouseover = () => {
    const hoverText = Object.assign(document.body.appendChild(document.createElement('span')), {
        textContent: 'Visite meu perfil no LinkedIn!',
        style: `position:fixed;background:#f0f0f0;padding:5px;border:1px solid #ccc;border-radius:5px;top:${linkedinLink.getBoundingClientRect().top - 30}px;left:${linkedinLink.getBoundingClientRect().left}px`,
        id: 'hover-text'
    });
};
linkedinLink.onmouseout = () => document.getElementById('hover-text')?.remove();

/*Link de certificados */

const CertLink = document.querySelector('#educacao a');

CertLink.onmouseover = () => {
    const hoverText = Object.assign(document.body.appendChild(document.createElement('span')), {
        textContent: 'Insira suas identificações na parte de comentários da solicitação de acesso, por gentileza.',
        style: `position:fixed;background:#f0f0f0;padding:5px;border:1px solid #ccc;border-radius:5px;top:${CertLink.getBoundingClientRect().top - 50}px;left:${CertLink.getBoundingClientRect().left}px`,
        id: 'hover-text'
    });
};
CertLink.onmouseout = () => document.getElementById('hover-text')?.remove();

