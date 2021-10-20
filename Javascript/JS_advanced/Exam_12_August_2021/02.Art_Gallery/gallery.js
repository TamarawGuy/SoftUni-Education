class ArtGallery {
    constructor(creator) {
        this.creator = creator;
        this.possibleArticles = { 'picture': 200, 'photo': 50, 'item': 250 };
        this.listOfArticles = [];
        this.guests = [];
    }

    addArticle(articleModel, articleName, quantity) {
        articleModel = articleModel.toLowerCase();

        if (!this.possibleArticles.hasOwnProperty(articleModel)) {
            throw new Error(`This article model is not included in this gallery!`);
        }
        else {
            let obj = this.listOfArticles.find(e => e.articleName === articleName && e.articleModel === articleModel);

            if (obj != undefined) {
                obj.quantity += quantity;
            }

            else {
                this.listOfArticles.push({ articleModel, articleName, quantity });
            }
            return `Successfully added article ${articleName} with a new quantity- ${quantity}.`;
        }
    }

    inviteGuest(guestName, personality) {
        let guest = this.guests.find(g => g.guestName === guestName);

        if (guest != undefined) {
            throw new Error(`${guestName} has already been invited.`);
        }
        else {
            let obj = {
                guestName: guestName,
                points: 0,
                purchaseArticle: 0
            }
            if (personality === 'Vip') {
                obj.points = 500;
            }

            else if (personality === 'Middle') {
                obj.points = 250;
            }
            else {
                obj.points = 50;
            }
            this.guests.push(obj);
            return `You have successfully invited ${guestName}!`;
        }
    }

    buyArticle(articleModel, articleName, guestName) {
        let guest = this.guests.find(g => g.guestName === guestName);

        if (guest == undefined) {
            return 'This guest is not invited.';
        }

        let obj = this.listOfArticles.find(e => e.articleName === articleName);

        if (obj == undefined) {
            throw new Error('This article is not found.');
        }

        obj = this.listOfArticles.find(e => e.articleName === articleName && e.articleModel === articleModel);
        if (obj == undefined) {
            throw new Error('This article is not found.');
        }

        else {
            if (obj.quantity <= 0) {
                return `The ${articleName} is not available.`;
            }

            let guestPoints = guest.points;
            let articlePoints = this.possibleArticles[articleModel];

            if (guestPoints < articlePoints) {
                return 'You need to more points to purchase the article.'
            }
            else {
                this.guests.forEach(g => {
                    if (g.guestName === guestName) {
                        g.points -= articlePoints;
                        g.purchaseArticle += 1;
                    }
                });

                this.listOfArticles.forEach(a => {
                    if (a.articleName === articleName && a.articleModel === articleModel) {
                        a.quantity -= 1;
                    }
                });

                return `${guestName} successfully purchased the article worth ${articlePoints} points.`;
            }
        }
    }

    showGalleryInfo(criteria) {
        if (criteria === 'article') {
            let result = '';
            result += 'Articles information:' + '\n';

            this.listOfArticles.forEach(a => {
                result += `${a.articleModel} - ${a.articleName} - ${a.quantity}` + '\n';
            });
            result = result.slice(0, -1);

            return result;
        }
        else {
            let result = '';
            result += 'Guests information:' + '\n';

            this.guests.forEach(g => {
                result += `${g.guestName} - ${g.purchaseArticle}` + '\n';
            });

            result = result.slice(0, -1);

            return result;
        }
    }
}


const artGallery = new ArtGallery('Curtis Mayfield');
artGallery.addArticle('picture', 'Mona Liza', 3);
artGallery.addArticle('Item', 'Ancient vase', 2);
artGallery.addArticle('picture', 'Mona Liza', 1);
artGallery.inviteGuest('John', 'Vip');
artGallery.inviteGuest('Peter', 'Middle');
artGallery.buyArticle('picture', 'Mona Liza', 'John');
artGallery.buyArticle('item', 'Ancient vase', 'Peter');
console.log(artGallery.showGalleryInfo('article'));
console.log(artGallery.showGalleryInfo('guest'));


