import { AppComponent } from './app.component';
import { ListarModule } from './components/nav/listar/listar.module';
import { CadastrarModule } from './components/nav/cadastrar/cadastrar.module';
import { HomeComponent } from './components/nav/cadastrar/home/home.component';
import { ItensComponent } from './components/nav/cadastrar/itens/itens.component';
import { NgModule, Component } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { NavComponent } from './components/nav/nav.component';



const routes: Routes = [
  //lazy loading so funciona com  modulos e não com components 
  {
    path: '', component: HomeComponent
  },
  {
    path: 'cadastrar',
    loadChildren: () => import('./components/nav/cadastrar/cadastrar.module').then(m => m.CadastrarModule)


  },
  {
    path: 'listar',
    loadChildren: () => import('./components/nav/listar/listar.module').then(m => m.ListarModule)
  }





];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
