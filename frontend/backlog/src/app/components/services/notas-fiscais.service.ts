import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { NotaFiscal } from '../interface/notaFiscal.interface';

@Injectable({
  providedIn: 'root'
})
export class NotasFiscaisService {

  constructor(public http: HttpClient) { }

  private httpOptions = { headers: new HttpHeaders({ 'Content-Type': 'application/json' }) };
  private geralUrl = 'http://localhost:8000/notas_fiscais/'


  getAll(): Observable<NotaFiscal[]> {
    return this.http.get<NotaFiscal[]>(this.geralUrl, this.httpOptions)
  }

  get(id: number): Observable<NotaFiscal> {
    let url = `${this.geralUrl}/${id}`;
    return this.http.get<NotaFiscal>(url)
  }

  create(geral: NotaFiscal): Observable<NotaFiscal> {
    return this.http.post<NotaFiscal>(this.geralUrl, geral, this.httpOptions)
  }

  delete(item: NotaFiscal | number): Observable<NotaFiscal> {
    const id = typeof item == 'number' ? item : item.id_nota_fiscal
    const url = `${this.geralUrl}/${id}`;
    return this.http.delete<NotaFiscal>(url, this.httpOptions)
  }
  // edit(item: NotaFiscal | number) {
  //   const id = typeof item == 'number' ? item : item.id
  // }

  update(item: NotaFiscal): Observable<any> {
    const url = `${this.geralUrl}/${item.id_nota_fiscal}`;
    return this.http.put<NotaFiscal>(url, item, this.httpOptions);
  }
}
