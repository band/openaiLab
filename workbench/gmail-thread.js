function extractGmailThread() {
    var subject = 'Your Subject Here';
    var threads = GmailApp.search('subject:' + subject);
    var messages = threads[0].getMessages();
    for (var i = 0; i < messages.length; i++) {
        Logger.log('From: ' + messages[i].getFrom() + ' Date: ' + messages[i].getDate());
        Logger.log('Message: ' + messages[i].getPlainBody());
    }
}