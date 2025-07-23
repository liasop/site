document.addEventListener('DOMContentLoaded', function() {
    const nav = `
        <div class="sidebar">
            <nav>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="works.html">Works</a></li>
                    <li><a href="about.html">About</a></li>
                    <li><a href="contact.html">Contact</a></li>
                    <li class="blog-entries">
                        <a href="7.22.25.html">7.22.25</a>
                    </li>
                </ul>
            </nav>
        </div>
    `;
    
    // Insert the navigation at the start of the body
    document.body.insertAdjacentHTML('afterbegin', nav);
}); 