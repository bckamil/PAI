const a = require('axios');
const $ = require('cheerio');

const url = 'butelki-puszki-belgia,c2,pl.html'

let axios = a.create({
  baseURL: 'https://smakpiwa.pl/'
});


class WebScraper {
  constructor(url) {
    this.startUrl = url;
    this.shopProducts = [];
    this.shopPaginationLinks = [];
    this.visitedLinks = [];
  }

  isNumeric(value) {
    return /^\d+$/.test(value);
  }

  setPaginationLinks(html) {
    let pagePagination = $('.abs-pagination-steps > .pagination > li > a', html);

    for (let index = 0; index < pagePagination.length; index++) {
      if (this.isNumeric(pagePagination[index].children[0].data) &&
        !this.shopPaginationLinks.includes(pagePagination[index].attribs.href) &&
        !this.visitedLinks.includes(pagePagination[index].attribs.href)
      ) {
        this.shopPaginationLinks.push(pagePagination[index].attribs.href);
      }
    }
  }

  getLink() {
    return this.shopPaginationLinks.shift()
  }

  addProducts(html) {
    let products = $('.abs-layout-product-full', html);
    for (let index = 0; index < products.length; index++) {
      let name = $('.abs-product-name', products[index]).text().trim().replace(/\s\s+/g, ' ');
      let details = $('.abs-col-details-description-attributes .list-group-item', products[index]);

      let capacityValue
      for (let index = 0; index < details.length; index++) {
        if ($('.abs-list-label', details[index]).text() === 'Poj.:') {
          capacityValue = $('.abs-list-value', details[index]).text().replace(',', '.');
          if (capacityValue.includes('ml')) {
            capacityValue = parseFloat(capacityValue);
          } else {
            capacityValue = parseFloat(capacityValue) * 1000;
          }
        }
      }

      let price = parseFloat($('.abs-item-price-amount', products[index]).text().replace(',', '.'));

      let product = {
        name: name,
        capacity: capacityValue,
        price: price,
        unitPrice: price / (capacityValue / 100)
      }

      this.shopProducts.push(product)
    }
  }

  showResults() {
    this.shopProducts = this.shopProducts.sort(function(a, b) {
      if (a.unitPrice < b.unitPrice) return -1;
      if (a.unitPrice > b.unitPrice) return 1;
      return 0;
    });

    for (let index = 0; index < this.shopProducts.length; index++) {
      const product = this.shopProducts[index];
      console.log('-----------------------------------------------')
      console.log(`${index + 1}:`)
      console.log(`Name: ${product.name}`)
      console.log(`Capacity: ${product.capacity} ml`)
      console.log(`Price: ${product.price} PLN`)
      console.log(`Price/unit (100 ml): ${product.unitPrice.toFixed(2)} PLN`)
    }
  }

  async start() {
    await axios(this.startUrl)
      .then(response => {
        const html = response.data;
        this.setPaginationLinks(html);
      })
      .catch(err => {
        console.log(err)
      })

    while (true) {
      let link = this.getLink();

      if (link) {
        const response = await axios(link);
        this.visitedLinks.push(link);

        const htmlPage = response.data;
        this.setPaginationLinks(htmlPage);
        this.addProducts(htmlPage);
      } else {
        break;
      }
    }

    this.showResults()
  }
}

ws = new WebScraper(url)
ws.start()
