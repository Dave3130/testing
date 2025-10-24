# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
bstack1l1_opy_ (u"ࠢࠣࠤࠍࡔࡾࡺࡥࡴࡶࠣࡸࡪࡹࡴࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡮ࡥ࡭ࡲࡨࡶࠥࡻࡳࡪࡰࡪࠤࡩ࡯ࡲࡦࡥࡷࠤࡵࡿࡴࡦࡵࡷࠤ࡭ࡵ࡯࡬ࡵ࠱ࠎࠧࠨࠢॅ")
import sys
import io
import os
from contextlib import redirect_stdout, redirect_stderr
def bstack11ll1l11_opy_(bstack11ll1l1l_opy_=None, bstack11ll11l1_opy_=None):
    bstack1l1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡅࡲࡰࡱ࡫ࡣࡵࠢࡳࡽࡹ࡫ࡳࡵࠢࡷࡩࡸࡺࡳࠡࡷࡶ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠧࡴࠢ࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠤࡆࡖࡉࡴ࠰ࠍࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡵࡧࡶࡸࡤࡧࡲࡨࡵࠣࠬࡱ࡯ࡳࡵ࠮ࠣࡳࡵࡺࡩࡰࡰࡤࡰ࠮ࡀࠠࡄࡱࡰࡴࡱ࡫ࡴࡦࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡴࡾࡺࡥࡴࡶࠣࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠦࡩ࡯ࡥ࡯ࡹࡩ࡯࡮ࡨࠢࡳࡥࡹ࡮ࡳࠡࡣࡱࡨࠥ࡬࡬ࡢࡩࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡡ࡬ࡧࡶࠤࡵࡸࡥࡤࡧࡧࡩࡳࡩࡥࠡࡱࡹࡩࡷࠦࡴࡦࡵࡷࡣࡵࡧࡴࡩࡵࠣ࡭࡫ࠦࡢࡰࡶ࡫ࠤࡦࡸࡥࠡࡲࡵࡳࡻ࡯ࡤࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡺࡥࡴࡶࡢࡴࡦࡺࡨࡴࠢࠫࡰ࡮ࡹࡴࠡࡱࡵࠤࡸࡺࡲ࠭ࠢࡲࡴࡹ࡯࡯࡯ࡣ࡯࠭࠿ࠦࡔࡦࡵࡷࠤ࡫࡯࡬ࡦࠪࡶ࠭࠴ࡪࡩࡳࡧࡦࡸࡴࡸࡹࠩ࡫ࡨࡷ࠮ࠦࡴࡰࠢࡦࡳࡱࡲࡥࡤࡶࠣࡪࡷࡵ࡭࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡇࡦࡴࠠࡣࡧࠣࡥࠥࡹࡩ࡯ࡩ࡯ࡩࠥࡶࡡࡵࡪࠣࡷࡹࡸࡩ࡯ࡩࠣࡳࡷࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡱࡣࡷ࡬ࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡋࡪࡲࡴࡸࡥࡥࠢ࡬ࡪࠥࡺࡥࡴࡶࡢࡥࡷ࡭ࡳࠡ࡫ࡶࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩ࠴ࠊࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡥ࡫ࡦࡸ࠿ࠦࡃࡰ࡮࡯ࡩࡨࡺࡩࡰࡰࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡼ࡯ࡴࡩࠢ࡮ࡩࡾࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡵࡸࡧࡨ࡫ࡳࡴࠢࠫࡦࡴࡵ࡬ࠪ࠼࡛ࠣ࡭࡫ࡴࡩࡧࡵࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࡵࡸࡧࡨ࡫ࡥࡥࡧࡧࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡨࡵࡵ࡯ࡶࠣࠬ࡮ࡴࡴࠪ࠼ࠣࡒࡺࡳࡢࡦࡴࠣࡳ࡫ࠦࡴࡦࡵࡷࡷࠥࡩ࡯࡭࡮ࡨࡧࡹ࡫ࡤࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡰࡲࡨࡪ࡯ࡤࡴࠢࠫࡰ࡮ࡹࡴࠪ࠼ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤࡹ࡫ࡳࡵࠢࡱࡳࡩ࡫ࠠࡊࡆࡶࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡹ࡫ࡳࡵࡡࡩ࡭ࡱ࡫ࡳࠡࠪ࡯࡭ࡸࡺࠩ࠻ࠢࡏ࡭ࡸࡺࠠࡰࡨࠣࡹࡳ࡯ࡱࡶࡧࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࠦࡰࡢࡶ࡫ࡷࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥ࡫ࡲࡳࡱࡵࠤ࠭ࡹࡴࡳࠫ࠽ࠤࡊࡸࡲࡰࡴࠣࡱࡪࡹࡳࡢࡩࡨࠤ࡮࡬ࠠࡴࡷࡦࡧࡪࡹࡳࠡ࡫ࡶࠤࡋࡧ࡬ࡴࡧࠍࠤࠥࠦࠠࡆࡺࡤࡱࡵࡲࡥࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡃࡄ࠾ࠡࠥࠣࡇࡴࡲ࡬ࡦࡥࡷࠤ࡫ࡸ࡯࡮ࠢࡷࡩࡸࡺࠠࡱࡣࡷ࡬ࡸࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠿ࡀࡁࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡃࠠࡤࡱ࡯ࡰࡪࡩࡴࡠࡶࡨࡷࡹࡹ࡟ࡸ࡫ࡷ࡬ࡤࡶࡹࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࠬࡹ࡫ࡳࡵࡡࡳࡥࡹ࡮ࡳ࠾࡝ࠥࡸࡪࡹࡴࡴ࠱ࠥࡡ࠮ࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠿ࡀࡁࠤࡵࡸࡩ࡯ࡶࠫࡪࠧࡌ࡯ࡶࡰࡧࠤࢀࡸࡥࡴࡷ࡯ࡸࡸࡡࠧࡤࡱࡸࡲࡹ࠭࡝ࡾࠢࡷࡩࡸࡺࡳࠣࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࡃࡄ࠾ࠡࠥࠣࡇࡴࡲ࡬ࡦࡥࡷࠤࡼ࡯ࡴࡩࠢࡳࡽࡹ࡫ࡳࡵࠢࡤࡶ࡬ࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࡀࡁࡂࠥࡸࡥࡴࡷ࡯ࡸࡸࠦ࠽ࠡࡥࡲࡰࡱ࡫ࡣࡵࡡࡷࡩࡸࡺࡳࡠࡹ࡬ࡸ࡭ࡥࡰࡺࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷ࠭ࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠯࠰࠱ࠤࠥࠦࠠࠡࡶࡨࡷࡹࡥࡡࡳࡩࡶࡁࡠࠨࡴࡦࡵࡷࡷ࠴ࠨࠬࠡࠤ࠰࠱ࡩࡸࡩࡷࡧࡵࠦ࠱ࠦࠢࡤࡪࡵࡳࡲ࡫ࠢ࡞࠮ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠳࠴࠮ࠡࠫࠍࠤࠥࠦࠠࠣࠤࠥॆ")
    try:
        import pytest
        if bstack11ll1l1l_opy_ is not None:
            args = list(bstack11ll1l1l_opy_)
        elif bstack11ll11l1_opy_ is not None:
            if isinstance(bstack11ll11l1_opy_, str):
                args = [bstack11ll11l1_opy_]
            elif isinstance(bstack11ll11l1_opy_, list):
                args = list(bstack11ll11l1_opy_)
            else:
                args = [bstack1l1_opy_ (u"ࠤ࠱ࠦे")]
        else:
            args = [bstack1l1_opy_ (u"ࠥ࠲ࠧै")]
        bstack11ll111l_opy_ = args + [
            bstack1l1_opy_ (u"ࠦ࠲࠳ࡣࡰ࡮࡯ࡩࡨࡺ࠭ࡰࡰ࡯ࡽࠧॉ"),
        ]
        class bstack11ll1ll1_opy_:
            bstack1l1_opy_ (u"ࠧࠨࠢࡑࡻࡷࡩࡸࡺࠠࡱ࡮ࡸ࡫࡮ࡴࠠࡵࡪࡤࡸࠥࡩࡡࡱࡶࡸࡶࡪࡹࠠࡤࡱ࡯ࡰࡪࡩࡴࡦࡦࠣࡸࡪࡹࡴࠡ࡫ࡷࡩࡲࡹ࠮ࠣࠤࠥॊ")
            def __init__(self):
                self.bstack11ll1111_opy_ = []
                self.test_files = set()
                self.bstack11ll11ll_opy_ = None
            def pytest_collection_finish(self, session):
                bstack1l1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡍࡵ࡯࡬ࠢࡦࡥࡱࡲࡥࡥࠢࡤࡪࡹ࡫ࡲࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡯ࡳࠡࡨ࡬ࡲ࡮ࡹࡨࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡃࡢࡲࡷࡹࡷ࡫ࡳࠡࡣ࡯ࡰࠥࡩ࡯࡭࡮ࡨࡧࡹ࡫ࡤࠡࡶࡨࡷࡹࠦࡩࡵࡧࡰࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦो")
                try:
                    for item in session.items:
                        nodeid = item.nodeid
                        self.bstack11ll1111_opy_.append(nodeid)
                        if bstack1l1_opy_ (u"ࠢ࠻࠼ࠥौ") in nodeid:
                            file_path = nodeid.split(bstack1l1_opy_ (u"ࠣ࠼࠽्ࠦ"), 1)[0]
                            file_path = os.path.normpath(file_path).replace(bstack1l1_opy_ (u"ࠩ࡟ࡠࠬॎ"), bstack1l1_opy_ (u"ࠪ࠳ࠬॏ"))
                            if file_path.endswith(bstack1l1_opy_ (u"ࠫ࠳ࡶࡹࠨॐ")):
                                self.test_files.add(file_path)
                except Exception as e:
                    self.bstack11ll11ll_opy_ = str(e)
        collector = bstack11ll1ll1_opy_()
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            exit_code = pytest.main(bstack11ll111l_opy_, plugins=[collector])
        if collector.bstack11ll11ll_opy_:
            return {
                bstack1l1_opy_ (u"ࠧࡹࡵࡤࡥࡨࡷࡸࠨ॑"): False,
                bstack1l1_opy_ (u"ࠨࡣࡰࡷࡱࡸ॒ࠧ"): 0,
                bstack1l1_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࡳࠣ॓"): [],
                bstack1l1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠧ॔"): [],
                bstack1l1_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣॕ"): bstack1l1_opy_ (u"ࠥࡇࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴࠠࡦࡴࡵࡳࡷࡀࠠࡼࡿࠥॖ").format(collector.bstack11ll11ll_opy_)
            }
        return {
            bstack1l1_opy_ (u"ࠦࡸࡻࡣࡤࡧࡶࡷࠧॗ"): True,
            bstack1l1_opy_ (u"ࠧࡩ࡯ࡶࡰࡷࠦक़"): len(collector.bstack11ll1111_opy_),
            bstack1l1_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࡹࠢख़"): collector.bstack11ll1111_opy_,
            bstack1l1_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡶࠦग़"): sorted(collector.test_files),
            bstack1l1_opy_ (u"ࠣࡧࡻ࡭ࡹࡥࡣࡰࡦࡨࠦज़"): exit_code
        }
    except Exception as e:
        error_msg = bstack1l1_opy_ (u"ࠤࡘࡲࡪࡾࡰࡦࡥࡷࡩࡩࠦࡥࡳࡴࡲࡶࠥ࡯࡮ࠡࡶࡨࡷࡹࠦࡣࡰ࡮࡯ࡩࡨࡺࡩࡰࡰ࠽ࠤࢀࢃࠢड़").format(str(e))
        return {
            bstack1l1_opy_ (u"ࠥࡷࡺࡩࡣࡦࡵࡶࠦढ़"): False,
            bstack1l1_opy_ (u"ࠦࡨࡵࡵ࡯ࡶࠥफ़"): 0,
            bstack1l1_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࡸࠨय़"): [],
            bstack1l1_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯࡬ࡦࡵࠥॠ"): [],
            bstack1l1_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨॡ"): error_msg
        }