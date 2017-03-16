/* 
 * Notification Soource Code: https://github.com/Microsoft/TypeScript/blob/release-2.2/lib/lib.webworker.d.ts
 */

function notify(title: string, body: string, icon: string) {
    if (Notification) {
        let notification = {},
            msg_title = title || '',
            msg_body = {'body': body || '', 'icon': icon || ''};

        Notification.requestPermission(function (permission) {
            if (permission === "granted") {
                notification = new Notification(msg_title, msg_body);
            }
        });
    }
}

notify(
    'Good Day!',
    'The is the message example. Please check the source code to see how to implement it.',
    'http://orig15.deviantart.net/a213/f/2014/191/e/e/lol_by_pikachumaster-d7q451j.gif'
);