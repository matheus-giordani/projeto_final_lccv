import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';

import { CadastrarRoutingModule } from './cadastrar-routing.module';
import { ItensComponent } from './itens/itens.component';
import { ProjetosComponent } from './projetos/projetos.component';
import { HomeComponent } from './home/home.component';
import { GeralComponent } from './geral/geral.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ListarComponent } from './itens/listar/listar.component';


@NgModule({
  declarations: [
    ItensComponent,
    ProjetosComponent,
    HomeComponent,
    GeralComponent,
    ListarComponent,


  ],
  imports: [
    CommonModule,
    CadastrarRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,


  ]


})
export class CadastrarModule { }
