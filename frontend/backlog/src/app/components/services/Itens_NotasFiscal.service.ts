import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Itens_NotasFiscal } from '../interface/itens_NotalFiscal.interface';


@Injectable({
  providedIn: 'root'
})
export class Itens_NotasFiscalService {

  constructor(public http: HttpClient) { }

  private httpOptions = { headers: new HttpHeaders({ 'Content-Type': 'application/json' }) };
  private geralUrl = 'http://localhost:8000/itens_notafiscal/'


  getAll(): Observable<Itens_NotasFiscal[]> {
    return this.http.get<Itens_NotasFiscal[]>(this.geralUrl, this.httpOptions)
  }

  get(id: number): Observable<Itens_NotasFiscal> {
    let url = `${this.geralUrl}/${id}`;
    return this.http.get<Itens_NotasFiscal>(url)
  }

  create(geral: Itens_NotasFiscal): Observable<Itens_NotasFiscal> {
    return this.http.post<Itens_NotasFiscal>(this.geralUrl, geral, this.httpOptions)
  }

  delete(item: Itens_NotasFiscal | number): Observable<Itens_NotasFiscal> {
    const id = typeof item == 'number' ? item : item.id_nota_fiscal
    const url = `${this.geralUrl}/${id}`;
    return this.http.delete<Itens_NotasFiscal>(url, this.httpOptions)
  }
  // edit(item: Itens_NotasFiscal | number) {
  //   const id = typeof item == 'number' ? item : item.id
  // }

  update(item: Itens_NotasFiscal): Observable<any> {
    const url = `${this.geralUrl}/${item.id_nota_fiscal}`;
    return this.http.put<Itens_NotasFiscal>(url, item, this.httpOptions);
  }
}
