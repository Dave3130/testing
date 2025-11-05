# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
bstack1lll11l_opy_ (u"ࠢࠣࠤࠍࡔࡾࡺࡥࡴࡶࠣࡸࡪࡹࡴࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡮ࡥ࡭ࡲࡨࡶࠥࡻࡳࡪࡰࡪࠤࡩ࡯ࡲࡦࡥࡷࠤࡵࡿࡴࡦࡵࡷࠤ࡭ࡵ࡯࡬ࡵ࠱ࠎࠧࠨࠢॅ")
import pytest
import io
import os
from contextlib import redirect_stdout, redirect_stderr
import subprocess
import sys
def bstack11ll1l1l_opy_(bstack11ll11ll_opy_=None, bstack11ll1l11_opy_=None):
    bstack1lll11l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡅࡲࡰࡱ࡫ࡣࡵࠢࡳࡽࡹ࡫ࡳࡵࠢࡷࡩࡸࡺࡳࠡࡷࡶ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠧࡴࠢ࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠤࡆࡖࡉࡴ࠰ࠍࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡵࡧࡶࡸࡤࡧࡲࡨࡵࠣࠬࡱ࡯ࡳࡵ࠮ࠣࡳࡵࡺࡩࡰࡰࡤࡰ࠮ࡀࠠࡄࡱࡰࡴࡱ࡫ࡴࡦࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡴࡾࡺࡥࡴࡶࠣࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠦࡩ࡯ࡥ࡯ࡹࡩ࡯࡮ࡨࠢࡳࡥࡹ࡮ࡳࠡࡣࡱࡨࠥ࡬࡬ࡢࡩࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡡ࡬ࡧࡶࠤࡵࡸࡥࡤࡧࡧࡩࡳࡩࡥࠡࡱࡹࡩࡷࠦࡴࡦࡵࡷࡣࡵࡧࡴࡩࡵࠣ࡭࡫ࠦࡢࡰࡶ࡫ࠤࡦࡸࡥࠡࡲࡵࡳࡻ࡯ࡤࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡺࡥࡴࡶࡢࡴࡦࡺࡨࡴࠢࠫࡰ࡮ࡹࡴࠡࡱࡵࠤࡸࡺࡲ࠭ࠢࡲࡴࡹ࡯࡯࡯ࡣ࡯࠭࠿ࠦࡔࡦࡵࡷࠤ࡫࡯࡬ࡦࠪࡶ࠭࠴ࡪࡩࡳࡧࡦࡸࡴࡸࡹࠩ࡫ࡨࡷ࠮ࠦࡴࡰࠢࡦࡳࡱࡲࡥࡤࡶࠣࡪࡷࡵ࡭࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡇࡦࡴࠠࡣࡧࠣࡥࠥࡹࡩ࡯ࡩ࡯ࡩࠥࡶࡡࡵࡪࠣࡷࡹࡸࡩ࡯ࡩࠣࡳࡷࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡱࡣࡷ࡬ࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡋࡪࡲࡴࡸࡥࡥࠢ࡬ࡪࠥࡺࡥࡴࡶࡢࡥࡷ࡭ࡳࠡ࡫ࡶࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩ࠴ࠊࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡥ࡫ࡦࡸ࠿ࠦࡃࡰ࡮࡯ࡩࡨࡺࡩࡰࡰࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡼ࡯ࡴࡩࠢ࡮ࡩࡾࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡵࡸࡧࡨ࡫ࡳࡴࠢࠫࡦࡴࡵ࡬ࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡦࡳࡺࡴࡴࠡࠪ࡬ࡲࡹ࠯ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠ࡯ࡱࡧࡩ࡮ࡪࡳࠡࠪ࡯࡭ࡸࡺࠩࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠥ࠮࡬ࡪࡵࡷ࠭ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥ࡫ࡲࡳࡱࡵࠤ࠭ࡹࡴࡳࠫࠍࠤࠥࠦࠠࠣࠤࠥॆ")
    try:
        if bstack11ll11ll_opy_ is not None:
            args = list(bstack11ll11ll_opy_)
        elif bstack11ll1l11_opy_ is not None:
            if isinstance(bstack11ll1l11_opy_, str):
                args = [bstack11ll1l11_opy_]
            elif isinstance(bstack11ll1l11_opy_, list):
                args = list(bstack11ll1l11_opy_)
            else:
                args = [bstack1lll11l_opy_ (u"ࠤ࠱ࠦे")]
        else:
            args = [bstack1lll11l_opy_ (u"ࠥ࠲ࠧै")]
        bstack11ll11l1_opy_ = args + [
            bstack1lll11l_opy_ (u"ࠦ࠲࠳ࡣࡰ࡮࡯ࡩࡨࡺ࠭ࡰࡰ࡯ࡽࠧॉ"),
            bstack1lll11l_opy_ (u"ࠧ࠳࠭ࡲࡷ࡬ࡩࡹࠨॊ")
        ]
        class bstack11ll1111_opy_:
            bstack1lll11l_opy_ (u"ࠨࠢࠣࡒࡼࡸࡪࡹࡴࠡࡲ࡯ࡹ࡬࡯࡮ࠡࡶ࡫ࡥࡹࠦࡣࡢࡲࡷࡹࡷ࡫ࡳࠡࡥࡲࡰࡱ࡫ࡣࡵࡧࡧࠤࡹ࡫ࡳࡵࠢ࡬ࡸࡪࡳࡳ࠯ࠤࠥࠦो")
            def __init__(self):
                self.bstack11ll1lll_opy_ = []
                self.test_files = set()
                self.bstack11ll1ll1_opy_ = None
            def pytest_collection_finish(self, session):
                bstack1lll11l_opy_ (u"ࠢࠣࠤࡋࡳࡴࡱࠠࡤࡣ࡯ࡰࡪࡪࠠࡢࡨࡷࡩࡷࠦࡣࡰ࡮࡯ࡩࡨࡺࡩࡰࡰࠣ࡭ࡸࠦࡦࡪࡰ࡬ࡷ࡭࡫ࡤ࠯ࠤࠥࠦौ")
                try:
                    for item in session.items:
                        nodeid = item.nodeid
                        self.bstack11ll1lll_opy_.append(nodeid)
                        if bstack1lll11l_opy_ (u"ࠣ࠼࠽्ࠦ") in nodeid:
                            file_path = nodeid.split(bstack1lll11l_opy_ (u"ࠤ࠽࠾ࠧॎ"), 1)[0]
                            if file_path.endswith(bstack1lll11l_opy_ (u"ࠪ࠲ࡵࡿࠧॏ")):
                                self.test_files.add(file_path)
                except Exception as e:
                    self.bstack11ll1ll1_opy_ = str(e)
        collector = bstack11ll1111_opy_()
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            exit_code = pytest.main(bstack11ll11l1_opy_, plugins=[collector])
        if collector.bstack11ll1ll1_opy_:
            return {bstack1lll11l_opy_ (u"ࠦࡸࡻࡣࡤࡧࡶࡷࠧॐ"): False, bstack1lll11l_opy_ (u"ࠧࡩ࡯ࡶࡰࡷࠦ॑"): 0, bstack1lll11l_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࡹ॒ࠢ"): [], bstack1lll11l_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡶࠦ॓"): [], bstack1lll11l_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢ॔"): bstack1lll11l_opy_ (u"ࠤࡆࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࠦࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠤॕ").format(collector.bstack11ll1ll1_opy_)}
        return {
            bstack1lll11l_opy_ (u"ࠥࡷࡺࡩࡣࡦࡵࡶࠦॖ"): True,
            bstack1lll11l_opy_ (u"ࠦࡨࡵࡵ࡯ࡶࠥॗ"): len(collector.bstack11ll1lll_opy_),
            bstack1lll11l_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࡸࠨक़"): collector.bstack11ll1lll_opy_,
            bstack1lll11l_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯࡬ࡦࡵࠥख़"): sorted(collector.test_files),
            bstack1lll11l_opy_ (u"ࠢࡦࡺ࡬ࡸࡤࡩ࡯ࡥࡧࠥग़"): exit_code
        }
    except Exception as e:
        return {bstack1lll11l_opy_ (u"ࠣࡵࡸࡧࡨ࡫ࡳࡴࠤज़"): False, bstack1lll11l_opy_ (u"ࠤࡦࡳࡺࡴࡴࠣड़"): 0, bstack1lll11l_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࡶࠦढ़"): [], bstack1lll11l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡩ࡭ࡱ࡫ࡳࠣफ़"): [], bstack1lll11l_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦय़"): bstack1lll11l_opy_ (u"ࠨࡕ࡯ࡧࡻࡴࡪࡩࡴࡦࡦࠣࡩࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡺࡥࡴࡶࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠦॠ").format(e)}