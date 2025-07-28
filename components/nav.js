document.addEventListener('DOMContentLoaded', function() {
    // Check if we're in a subdirectory by looking at the current path
    const isInBlogDir = window.location.pathname.includes('/blog/');
    const prefix = isInBlogDir ? '../' : '';
    
    const nav = `
        <div class="sidebar">
            <nav>
                <ul>
                    <li><a href="${prefix}index.html">Home</a></li>
                    <li><a href="${prefix}works.html">Works</a></li>
                    <li><a href="${prefix}about.html">About</a></li>
                    <li><a href="${prefix}contact.html">Contact</a></li>
                    <li class="blog-entries">
                        <a href="${prefix}blog/7.27.25.html">7.27.25</a>
                        <a href="${prefix}blog/7.26.27.html">7.26.27</a>
                        <a href="${prefix}blog/7.25.25.html">7.25.25</a>
                        <a href="${prefix}blog/7.24.25.html">7.24.25</a>
                        <a href="${prefix}blog/7.23.25.html">7.23.25</a>
                        <a href="${prefix}blog/7.22.25.html">7.22.25</a>
                    </li>
                </ul>
            </nav>
        </div>
    `;
    
    // Insert the navigation at the start of the body
    document.body.insertAdjacentHTML('afterbegin', nav);
}); 