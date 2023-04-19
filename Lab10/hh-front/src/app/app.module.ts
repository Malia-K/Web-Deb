import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { CompanyListComponent } from './company-list/company-list.component'
import { RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { TopBarComponent } from './top-bar/top-bar.component';
import { VacancyListComponent } from './vacancy-list/vacancy-list.component';
import { CompanyDetailComponent } from './company-detail/company-detail.component';

@NgModule({
  declarations: [
    AppComponent,
    CompanyListComponent,
    TopBarComponent,
    VacancyListComponent,
    CompanyDetailComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    RouterModule.forRoot([
      { path: 'companies', component: CompanyListComponent},
      { path: 'vacancies', component: VacancyListComponent},
      { path: 'companies/:id', component: VacancyListComponent},
      { path: '', redirectTo:"companies", pathMatch: 'full'},
      // { path: '', component: ProductDetailsComponent },
    ])
  ],
  
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
