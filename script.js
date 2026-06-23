// 页面加载完成后的动画
document.addEventListener("DOMContentLoaded", function() {
    // 技能条动画
    const skillBars = document.querySelectorAll(".skill-fill");
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.width = entry.target.style.width;
            }
        });
    }, { threshold: 0.5 });

    skillBars.forEach(bar => observer.observe(bar));

    // 导航栏滚动效果
    let lastScroll = 0;
    window.addEventListener("scroll", function() {
        const nav = document.querySelector("nav");
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 100) {
            nav.style.background = "rgba(30, 30, 47, 0.98)";
        } else {
            nav.style.background = "rgba(30, 30, 47, 0.95)";
        }
        
        lastScroll = currentScroll;
    });

    // 平滑滚动
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute("href"));
            if (target) {
                target.scrollIntoView({ behavior: "smooth" });
            }
        });
    });
});
