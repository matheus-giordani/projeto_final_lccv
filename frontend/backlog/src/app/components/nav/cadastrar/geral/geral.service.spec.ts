import { TestBed } from '@angular/core/testing';

import { BensService } from '../../../services/bens.service';

describe('GeralService', () => {
  let service: BensService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(BensService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
