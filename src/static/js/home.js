$(document).ready(
    function () {
        $.ajax({
            url: '/api/database/news?limit=6',
            type: 'GET',
            success: data => {
                var newsList = document.getElementById('news');
                data.news.forEach(news_obj => {
                    var news_block = document.createElement('div');
                    news_block.className = 'col mb-2 mt-2';
                    news_block.innerHTML = `
                            <div class="card h-100 text-white bg-dark">
                                <img src="${news_obj.image}" class="card-img-top" alt="Нет изображения">
                                
                                <div class="card-body d-flex h-100 flex-column">
                                    <h5 class="card-title">${news_obj.title}</h5>
                                    <p class="card-text flex-grow-1">${news_obj.content}</p>
                                    <div class="text-end d-flex flex-row justify-content-between">
                                        <a class="btn btn-primary" href="#" role="button">Читать новость</a>
                                        <span class="badge pt-3">${news_obj.created_at.toString().split('T')[0]}</span>
                                    </div>
                                </div>
                            </div>
                    `;
                    newsList.appendChild(news_block);
                });
            },
            error: errorMessage => {
                console.log(errorMessage)
            }
        });
    }
);

