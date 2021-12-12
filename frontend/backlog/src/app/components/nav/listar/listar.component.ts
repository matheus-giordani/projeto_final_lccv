import { Itens_NotasFiscalService } from './../../services/Itens_NotasFiscal.service';
import { FornecedorService } from './../../services/fornecedor.service';
import { NotaFiscal } from './../../interface/notaFiscal.interface';
import { Itens_NotasFiscal } from './../../interface/itens_NotalFiscal.interface';
import { Fornecedores } from './../../interface/fornecedor.interface';
import { NotasFiscaisService } from './../../services/notas-fiscais.service';
import { BensService } from '../../services/bens.service';
import { Component, OnInit } from '@angular/core';
import { Bens } from '../../interface/bens.interface';
import { FormControl, Validators, FormGroup } from '@angular/forms';


import { Location } from '@angular/common';
import { forkJoin } from 'rxjs';

interface DadosTabela {
  Numero: number;
  Prestador: string;
  Valor: number
}

@Component({
  selector: 'app-listar',
  templateUrl: './listar.component.html',
  styleUrls: ['./listar.component.scss']
})
export class ListarComponent implements OnInit {
  editForm!: FormGroup
  bens!: Bens[];//get bens
  NotasFiscais!: NotaFiscal[];//get notas fiscais
  fornecedor!: Fornecedores[];
  itens_NotasFiscal!: Itens_NotasFiscal[];
  notaFiscal!: NotaFiscal[];
  dadosTabela: DadosTabela[] = [];


  constructor(private NotasFiscaisService: NotasFiscaisService,
    private bensService: BensService,
    private fornecedoresService: FornecedorService,
    private itens_NotasFiscalService: Itens_NotasFiscalService,
    private location: Location) { }


  ngOnInit(): void {
    forkJoin([this.bensService.getAll(),
    this.NotasFiscaisService.getAll(),
    this.fornecedoresService.getAll(),
    this.itens_NotasFiscalService.getAll()]).subscribe(resultado => {
      const [bens, notasfiscais, fornecedores, itens_NotaFiscal] = resultado
      if (!bens) {
        return;
      }
      bens.forEach(element => {

        if (!bens || !notasfiscais || !fornecedores || !itens_NotaFiscal) {
          return;
        }
        let item_nota_fiscal: Itens_NotasFiscal | undefined
        if (itens_NotaFiscal) {

          item_nota_fiscal = itens_NotaFiscal.find(g => g.id_item_nota_fiscal == element.id_item_nota_fiscal)
        }
        let notaFiscal: NotaFiscal | undefined
        if (notasfiscais) {
          notaFiscal = notasfiscais.find(g => g.id_nota_fiscal == item_nota_fiscal?.id_nota_fiscal)

        }
        let fornecedor: Fornecedores | undefined
        if (fornecedores) {

          fornecedor = fornecedores.find(g => g.id_fornecedor == notaFiscal?.id_fornecedor)
        }
        if (item_nota_fiscal && notaFiscal && fornecedor) {
          this.dadosTabela.push({
            'Numero': notaFiscal?.numero, 'Prestador': fornecedor?.razao_social,
            'Valor': item_nota_fiscal?.qtd * item_nota_fiscal?.valor_unitario
          })

        }


      });
    })
  }




  onSubmit() {
    const newRegister = this.editForm.value;
    this.bensService.update(newRegister)
      .subscribe(_ => this.goBack());
    this.goBack()//pra fazer ele ir e voltar pra mesma pagina


  }

  goBack() {
    this.location.back();
  }


}