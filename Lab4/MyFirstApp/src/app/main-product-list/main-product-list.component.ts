import { Component } from '@angular/core';

import { main_products } from '../main-product';

@Component({
  selector: 'app-main-product-list',
  templateUrl: './main-product-list.component.html',
  styleUrls: ['./main-product-list.component.css']
})
export class MainProductListComponent {
  main_products = [...main_products];

  share() {
    window.alert('The product has been shared!');
  }

}
