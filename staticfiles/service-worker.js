self.addEventListener('install', event => {
    event.waitUntil(
        caches.open('v1').then(cache => {
            return cache.addAll([
                '/',
                '/https://uniabujaflex.s3.amazonaws.com/static/home/images/logo.png',
                '/https://uniabujaflex.s3.amazonaws.com/static/home/images/logo.png',
                // Add other assets you want to cache
            ]);
        })
    );
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request);
        })
    );
});
