"""Generates the arm32 headers used by the gemm/gemv lib."""

import cc_emitter
import common
import neon_emitter
import quantized_mul_kernels_common


def Main():
  """."""
  cc = cc_emitter.CCEmitter()
  common.GenerateHeader(cc, 'gemmlowp_meta_quantized_mul_kernels_arm_32',
                        'GEMMLOWP_NEON_32')

  cc.EmitNamespaceBegin('gemmlowp')
  cc.EmitNamespaceBegin('meta')
  cc.EmitNewline()

  shapes = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
            (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3)]

  quantized_mul_kernels_common.GenerateKernels(cc, neon_emitter.NeonEmitter(),
                                               shapes)

  cc.EmitNamespaceEnd()
  cc.EmitNamespaceEnd()
  cc.EmitNewline()

  common.GenerateFooter(cc, 'Meta gemm for arm32 requires: GEMMLOWP_NEON_32!')


if __name__ == '__main__':
  Main()
