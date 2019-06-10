import { HttpClientModule } from '@angular/common/http';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule ,ReactiveFormsModule} from '@angular/forms';
import { HomeComponent } from './home/home.component';
import { TutorialsComponent } from './home/tutorials/tutorials.component';
import { JwtModule } from '@auth0/angular-jwt';
import { NgHttpLoaderModule } from 'ng-http-loader';
import { ScriptComponent } from './script/script.component';
import { ScriptSlideComponent } from './script/script-slide/script-slide.component';
import { ScriptCreateComponent } from './script/script-create/script-create.component';
import { ScriptEditComponent } from './script/script-edit/script-edit.component';

export function tokenGetter() {
  const token = localStorage.getItem('token');
  return token;
}

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    TutorialsComponent,
    ScriptComponent,
    ScriptSlideComponent,
    ScriptCreateComponent,
    ScriptEditComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    JwtModule.forRoot({
      config: {
        tokenGetter: tokenGetter,
        whitelistedDomains: ['localhost:8000'],
        blacklistedRoutes: ['']
      }
    }),
    RouterModule,
    FormsModule,
    ReactiveFormsModule,
    NgHttpLoaderModule.forRoot()
  
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

