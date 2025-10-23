# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
bstack11lll1_opy_ (u"ࠢࠣࠤࠍࡔࡾࡺࡥࡴࡶࠣࡸࡪࡹࡴࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡮ࡥ࡭ࡲࡨࡶࠥࡻࡳࡪࡰࡪࠤࡩ࡯ࡲࡦࡥࡷࠤࡵࡿࡴࡦࡵࡷࠤ࡭ࡵ࡯࡬ࡵ࠱ࠎࠧࠨࠢॅ")
import sys
import io
import os
from contextlib import redirect_stdout, redirect_stderr
def bstack11l1llll_opy_(bstack11ll11ll_opy_=None, bstack11ll1l11_opy_=None):
    bstack11lll1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡅࡲࡰࡱ࡫ࡣࡵࠢࡳࡽࡹ࡫ࡳࡵࠢࡷࡩࡸࡺࡳࠡࡷࡶ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠧࡴࠢ࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠤࡆࡖࡉࡴ࠰ࠍࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡵࡧࡶࡸࡤࡧࡲࡨࡵࠣࠬࡱ࡯ࡳࡵ࠮ࠣࡳࡵࡺࡩࡰࡰࡤࡰ࠮ࡀࠠࡄࡱࡰࡴࡱ࡫ࡴࡦࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡴࡾࡺࡥࡴࡶࠣࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠦࡩ࡯ࡥ࡯ࡹࡩ࡯࡮ࡨࠢࡳࡥࡹ࡮ࡳࠡࡣࡱࡨࠥ࡬࡬ࡢࡩࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡡ࡬ࡧࡶࠤࡵࡸࡥࡤࡧࡧࡩࡳࡩࡥࠡࡱࡹࡩࡷࠦࡴࡦࡵࡷࡣࡵࡧࡴࡩࡵࠣ࡭࡫ࠦࡢࡰࡶ࡫ࠤࡦࡸࡥࠡࡲࡵࡳࡻ࡯ࡤࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡺࡥࡴࡶࡢࡴࡦࡺࡨࡴࠢࠫࡰ࡮ࡹࡴࠡࡱࡵࠤࡸࡺࡲ࠭ࠢࡲࡴࡹ࡯࡯࡯ࡣ࡯࠭࠿ࠦࡔࡦࡵࡷࠤ࡫࡯࡬ࡦࠪࡶ࠭࠴ࡪࡩࡳࡧࡦࡸࡴࡸࡹࠩ࡫ࡨࡷ࠮ࠦࡴࡰࠢࡦࡳࡱࡲࡥࡤࡶࠣࡪࡷࡵ࡭࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡇࡦࡴࠠࡣࡧࠣࡥࠥࡹࡩ࡯ࡩ࡯ࡩࠥࡶࡡࡵࡪࠣࡷࡹࡸࡩ࡯ࡩࠣࡳࡷࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡱࡣࡷ࡬ࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡋࡪࡲࡴࡸࡥࡥࠢ࡬ࡪࠥࡺࡥࡴࡶࡢࡥࡷ࡭ࡳࠡ࡫ࡶࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩ࠴ࠊࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡥ࡫ࡦࡸ࠿ࠦࡃࡰ࡮࡯ࡩࡨࡺࡩࡰࡰࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡼ࡯ࡴࡩࠢ࡮ࡩࡾࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡵࡸࡧࡨ࡫ࡳࡴࠢࠫࡦࡴࡵ࡬ࠪ࠼࡛ࠣ࡭࡫ࡴࡩࡧࡵࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࡵࡸࡧࡨ࡫ࡥࡥࡧࡧࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡨࡵࡵ࡯ࡶࠣࠬ࡮ࡴࡴࠪ࠼ࠣࡒࡺࡳࡢࡦࡴࠣࡳ࡫ࠦࡴࡦࡵࡷࡷࠥࡩ࡯࡭࡮ࡨࡧࡹ࡫ࡤࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡰࡲࡨࡪ࡯ࡤࡴࠢࠫࡰ࡮ࡹࡴࠪ࠼ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤࡹ࡫ࡳࡵࠢࡱࡳࡩ࡫ࠠࡊࡆࡶࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡹ࡫ࡳࡵࡡࡩ࡭ࡱ࡫ࡳࠡࠪ࡯࡭ࡸࡺࠩ࠻ࠢࡏ࡭ࡸࡺࠠࡰࡨࠣࡹࡳ࡯ࡱࡶࡧࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࠦࡰࡢࡶ࡫ࡷࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥ࡫ࡲࡳࡱࡵࠤ࠭ࡹࡴࡳࠫ࠽ࠤࡊࡸࡲࡰࡴࠣࡱࡪࡹࡳࡢࡩࡨࠤ࡮࡬ࠠࡴࡷࡦࡧࡪࡹࡳࠡ࡫ࡶࠤࡋࡧ࡬ࡴࡧࠍࠤࠥࠦࠠࡆࡺࡤࡱࡵࡲࡥࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡃࡄ࠾ࠡࠥࠣࡇࡴࡲ࡬ࡦࡥࡷࠤ࡫ࡸ࡯࡮ࠢࡷࡩࡸࡺࠠࡱࡣࡷ࡬ࡸࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠿ࡀࡁࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡃࠠࡤࡱ࡯ࡰࡪࡩࡴࡠࡶࡨࡷࡹࡹ࡟ࡸ࡫ࡷ࡬ࡤࡶࡹࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࠬࡹ࡫ࡳࡵࡡࡳࡥࡹ࡮ࡳ࠾࡝ࠥࡸࡪࡹࡴࡴ࠱ࠥࡡ࠮ࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠿ࡀࡁࠤࡵࡸࡩ࡯ࡶࠫࡪࠧࡌ࡯ࡶࡰࡧࠤࢀࡸࡥࡴࡷ࡯ࡸࡸࡡࠧࡤࡱࡸࡲࡹ࠭࡝ࡾࠢࡷࡩࡸࡺࡳࠣࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࡃࡄ࠾ࠡࠥࠣࡇࡴࡲ࡬ࡦࡥࡷࠤࡼ࡯ࡴࡩࠢࡳࡽࡹ࡫ࡳࡵࠢࡤࡶ࡬ࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࡀࡁࡂࠥࡸࡥࡴࡷ࡯ࡸࡸࠦ࠽ࠡࡥࡲࡰࡱ࡫ࡣࡵࡡࡷࡩࡸࡺࡳࡠࡹ࡬ࡸ࡭ࡥࡰࡺࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷ࠭ࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠯࠰࠱ࠤࠥࠦࠠࠡࡶࡨࡷࡹࡥࡡࡳࡩࡶࡁࡠࠨࡴࡦࡵࡷࡷ࠴ࠨࠬࠡࠤ࠰࠱ࡩࡸࡩࡷࡧࡵࠦ࠱ࠦࠢࡤࡪࡵࡳࡲ࡫ࠢ࡞࠮ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠳࠴࠮ࠡࠫࠍࠤࠥࠦࠠࠣࠤࠥॆ")
    try:
        import pytest
        if bstack11ll11ll_opy_ is not None:
            args = list(bstack11ll11ll_opy_)
        elif bstack11ll1l11_opy_ is not None:
            if isinstance(bstack11ll1l11_opy_, str):
                args = [bstack11ll1l11_opy_]
            elif isinstance(bstack11ll1l11_opy_, list):
                args = list(bstack11ll1l11_opy_)
            else:
                args = [bstack11lll1_opy_ (u"ࠤ࠱ࠦे")]
        else:
            args = [bstack11lll1_opy_ (u"ࠥ࠲ࠧै")]
        bstack11ll111l_opy_ = args + [
            bstack11lll1_opy_ (u"ࠦ࠲࠳ࡣࡰ࡮࡯ࡩࡨࡺ࠭ࡰࡰ࡯ࡽࠧॉ"),
        ]
        class bstack11ll1ll1_opy_:
            bstack11lll1_opy_ (u"ࠧࠨࠢࡑࡻࡷࡩࡸࡺࠠࡱ࡮ࡸ࡫࡮ࡴࠠࡵࡪࡤࡸࠥࡩࡡࡱࡶࡸࡶࡪࡹࠠࡤࡱ࡯ࡰࡪࡩࡴࡦࡦࠣࡸࡪࡹࡴࠡ࡫ࡷࡩࡲࡹ࠮ࠣࠤࠥॊ")
            def __init__(self):
                self.bstack11l1ll1l_opy_ = []
                self.test_files = set()
                self.bstack11ll11l1_opy_ = None
            def pytest_collection_finish(self, session):
                bstack11lll1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡍࡵ࡯࡬ࠢࡦࡥࡱࡲࡥࡥࠢࡤࡪࡹ࡫ࡲࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡯ࡳࠡࡨ࡬ࡲ࡮ࡹࡨࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡃࡢࡲࡷࡹࡷ࡫ࡳࠡࡣ࡯ࡰࠥࡩ࡯࡭࡮ࡨࡧࡹ࡫ࡤࠡࡶࡨࡷࡹࠦࡩࡵࡧࡰࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦो")
                try:
                    for item in session.items:
                        nodeid = item.nodeid
                        self.bstack11l1ll1l_opy_.append(nodeid)
                        if bstack11lll1_opy_ (u"ࠢ࠻࠼ࠥौ") in nodeid:
                            file_path = nodeid.split(bstack11lll1_opy_ (u"ࠣ࠼࠽्ࠦ"), 1)[0]
                            file_path = os.path.normpath(file_path).replace(bstack11lll1_opy_ (u"ࠩ࡟ࡠࠬॎ"), bstack11lll1_opy_ (u"ࠪ࠳ࠬॏ"))
                            if file_path.endswith(bstack11lll1_opy_ (u"ࠫ࠳ࡶࡹࠨॐ")):
                                self.test_files.add(file_path)
                except Exception as e:
                    self.bstack11ll11l1_opy_ = str(e)
        collector = bstack11ll1ll1_opy_()
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            exit_code = pytest.main(bstack11ll111l_opy_, plugins=[collector])
        if collector.bstack11ll11l1_opy_:
            return {
                bstack11lll1_opy_ (u"ࠧࡹࡵࡤࡥࡨࡷࡸࠨ॑"): False,
                bstack11lll1_opy_ (u"ࠨࡣࡰࡷࡱࡸ॒ࠧ"): 0,
                bstack11lll1_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࡳࠣ॓"): [],
                bstack11lll1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠧ॔"): [],
                bstack11lll1_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣॕ"): bstack11lll1_opy_ (u"ࠥࡇࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴࠠࡦࡴࡵࡳࡷࡀࠠࡼࡿࠥॖ").format(collector.bstack11ll11l1_opy_)
            }
        return {
            bstack11lll1_opy_ (u"ࠦࡸࡻࡣࡤࡧࡶࡷࠧॗ"): True,
            bstack11lll1_opy_ (u"ࠧࡩ࡯ࡶࡰࡷࠦक़"): len(collector.bstack11l1ll1l_opy_),
            bstack11lll1_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࡹࠢख़"): collector.bstack11l1ll1l_opy_,
            bstack11lll1_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡶࠦग़"): sorted(collector.test_files),
            bstack11lll1_opy_ (u"ࠣࡧࡻ࡭ࡹࡥࡣࡰࡦࡨࠦज़"): exit_code
        }
    except Exception as e:
        error_msg = bstack11lll1_opy_ (u"ࠤࡘࡲࡪࡾࡰࡦࡥࡷࡩࡩࠦࡥࡳࡴࡲࡶࠥ࡯࡮ࠡࡶࡨࡷࡹࠦࡣࡰ࡮࡯ࡩࡨࡺࡩࡰࡰ࠽ࠤࢀࢃࠢड़").format(str(e))
        return {
            bstack11lll1_opy_ (u"ࠥࡷࡺࡩࡣࡦࡵࡶࠦढ़"): False,
            bstack11lll1_opy_ (u"ࠦࡨࡵࡵ࡯ࡶࠥफ़"): 0,
            bstack11lll1_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࡸࠨय़"): [],
            bstack11lll1_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯࡬ࡦࡵࠥॠ"): [],
            bstack11lll1_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨॡ"): error_msg
        }
def bstack11ll1l1l_opy_(cache_dir=bstack11lll1_opy_ (u"ࠨ࠰ࡳࡽࡹ࡫ࡳࡵࡡࡦࡥࡨ࡮ࡥࠨॢ")):
    bstack11lll1_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡊࡩࡹࠦࡴࡩࡧࠣࡰ࡮ࡹࡴࠡࡱࡩࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࠢࡱࡳࡩ࡫ࠠࡊࡆࡶࠤࡩ࡯ࡲࡦࡥࡷࡰࡾࠦࡦࡳࡱࡰࠤࡵࡿࡴࡦࡵࡷࠤࡨࡧࡣࡩࡧ࠱ࠎࠥࠦࠠࠡࡖ࡫࡭ࡸࠦࡩࡴࠢࡩࡥࡸࡺࡥࡳࠢࡷ࡬ࡦࡴࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥࡧ࡮ࡥࠢࡦࡥࡳࠦࡢࡦࠢࡸࡷࡪࡪࠠࡵࡱࠣࡵࡺ࡯ࡣ࡬࡮ࡼࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠊࠡࠢࠣࠤࡼ࡮ࡩࡤࡪࠣࡸࡪࡹࡴࡴࠢࡩࡥ࡮ࡲࡥࡥࠢࡺ࡭ࡹ࡮࡯ࡶࡶࠣ࡭ࡳࡼ࡯࡬࡫ࡱ࡫ࠥࡶࡹࡵࡧࡶࡸ࠳ࠐࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡧࡦࡩࡨࡦࡡࡧ࡭ࡷࠦࠨࡴࡶࡵ࠭࠿ࠦࡐࡢࡶ࡫ࠤࡹࡵࠠࡱࡻࡷࡩࡸࡺࠠࡤࡣࡦ࡬ࡪࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺ࠰ࠣࡈࡪ࡬ࡡࡶ࡮ࡷࠤࠬ࠴ࡰࡺࡶࡨࡷࡹࡥࡣࡢࡥ࡫ࡩࠬࠐࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦ࡬ࡪࡵࡷ࠾ࠥࡒࡩࡴࡶࠣࡳ࡫ࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࠤࡳࡵࡤࡦࠢࡌࡈࡸ࠲ࠠࡰࡴࠣࡩࡲࡶࡴࡺࠢ࡯࡭ࡸࡺࠠࡪࡨࠣࡲࡴࠦࡦࡢ࡫࡯ࡹࡷ࡫ࡳࠡࡥࡤࡧ࡭࡫ࡤࠋࠢࠣࠤࠥࡋࡸࡢ࡯ࡳࡰࡪࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࡀࡁࡂࠥࠩࠠࡒࡷ࡬ࡧࡰࠦࡣࡩࡧࡦ࡯ࠥࡵࡦࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹࠠࡧࡴࡲࡱࠥࡩࡡࡤࡪࡨࠎࠥࠦࠠࠡࠢࠣࠤࠥࡄ࠾࠿ࠢࡩࡥ࡮ࡲࡥࡥࡡࡱࡳࡩ࡫ࡩࡥࡵࠣࡁࠥ࡭ࡥࡵࡡࡦࡥࡨ࡮ࡥࡥࡡࡩࡥ࡮ࡲࡥࡥࡡࡱࡳࡩ࡫ࡩࡥࡵࠫ࠭ࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠾࠿ࡀࠣࡴࡷ࡯࡮ࡵࠪࡩࠦࡕࡸࡥࡷ࡫ࡲࡹࡸࡲࡹࠡࡨࡤ࡭ࡱ࡫ࡤ࠻ࠢࡾࡰࡪࡴࠨࡧࡣ࡬ࡰࡪࡪ࡟࡯ࡱࡧࡩ࡮ࡪࡳࠪࡿࠣࡸࡪࡹࡴࡴࠤࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥࡄ࠾࠿ࠢࡩࡳࡷࠦ࡮ࡰࡦࡨ࡭ࡩࠦࡩ࡯ࠢࡩࡥ࡮ࡲࡥࡥࡡࡱࡳࡩ࡫ࡩࡥࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠴࠮࠯ࠢࠣࠤࠥࠦࡰࡳ࡫ࡱࡸ࠭࡬ࠢࠡࠢ࠰ࠤࢀࡴ࡯ࡥࡧ࡬ࡨࢂࠨࠩࠋࠢࠣࠤࠥࠨࠢࠣॣ")
    import json
    bstack11ll1111_opy_ = os.path.join(cache_dir, bstack11lll1_opy_ (u"ࠪࡺࠬ।"), bstack11lll1_opy_ (u"ࠫࡨࡧࡣࡩࡧࠪ॥"), bstack11lll1_opy_ (u"ࠬࡲࡡࡴࡶࡩࡥ࡮ࡲࡥࡥࠩ०"))
    try:
        if os.path.exists(bstack11ll1111_opy_):
            with open(bstack11ll1111_opy_, bstack11lll1_opy_ (u"࠭ࡲࠨ१")) as f:
                bstack11l1lll1_opy_ = json.load(f)
                return list(bstack11l1lll1_opy_.keys())
        return []
    except Exception:
        return []