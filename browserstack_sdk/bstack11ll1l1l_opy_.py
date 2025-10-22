# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
bstack11l1l11_opy_ (u"ࠢࠣࠤࠍࡔࡾࡺࡥࡴࡶࠣࡸࡪࡹࡴࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡮ࡥ࡭ࡲࡨࡶࠥࡻࡳࡪࡰࡪࠤࡩ࡯ࡲࡦࡥࡷࠤࡵࡿࡴࡦࡵࡷࠤ࡭ࡵ࡯࡬ࡵ࠱ࠎࠧࠨࠢॅ")
import sys
import io
import os
from contextlib import redirect_stdout, redirect_stderr
def bstack11ll1111_opy_(bstack11ll11l1_opy_=None, bstack11l1lll1_opy_=None, bstack11ll11ll_opy_=False):
    bstack11l1l11_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡅࡲࡰࡱ࡫ࡣࡵࠢࡳࡽࡹ࡫ࡳࡵࠢࡷࡩࡸࡺࡳࠡࡷࡶ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠧࡴࠢ࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠤࡆࡖࡉࡴ࠰ࠍࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡵࡧࡶࡸࡤࡧࡲࡨࡵࠣࠬࡱ࡯ࡳࡵ࠮ࠣࡳࡵࡺࡩࡰࡰࡤࡰ࠮ࡀࠠࡄࡱࡰࡴࡱ࡫ࡴࡦࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡴࡾࡺࡥࡴࡶࠣࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠦࡩ࡯ࡥ࡯ࡹࡩ࡯࡮ࡨࠢࡳࡥࡹ࡮ࡳࠡࡣࡱࡨࠥ࡬࡬ࡢࡩࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡡ࡬ࡧࡶࠤࡵࡸࡥࡤࡧࡧࡩࡳࡩࡥࠡࡱࡹࡩࡷࠦࡴࡦࡵࡷࡣࡵࡧࡴࡩࡵࠣ࡭࡫ࠦࡢࡰࡶ࡫ࠤࡦࡸࡥࠡࡲࡵࡳࡻ࡯ࡤࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡺࡥࡴࡶࡢࡴࡦࡺࡨࡴࠢࠫࡰ࡮ࡹࡴࠡࡱࡵࠤࡸࡺࡲ࠭ࠢࡲࡴࡹ࡯࡯࡯ࡣ࡯࠭࠿ࠦࡔࡦࡵࡷࠤ࡫࡯࡬ࡦࠪࡶ࠭࠴ࡪࡩࡳࡧࡦࡸࡴࡸࡹࠩ࡫ࡨࡷ࠮ࠦࡴࡰࠢࡦࡳࡱࡲࡥࡤࡶࠣࡪࡷࡵ࡭࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡇࡦࡴࠠࡣࡧࠣࡥࠥࡹࡩ࡯ࡩ࡯ࡩࠥࡶࡡࡵࡪࠣࡷࡹࡸࡩ࡯ࡩࠣࡳࡷࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡱࡣࡷ࡬ࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡋࡪࡲࡴࡸࡥࡥࠢ࡬ࡪࠥࡺࡥࡴࡶࡢࡥࡷ࡭ࡳࠡ࡫ࡶࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡵ࡬ࡰࡪࡴࡴࠡࠪࡥࡳࡴࡲࠬࠡࡱࡳࡸ࡮ࡵ࡮ࡢ࡮ࠬ࠾ࠥࡏࡦࠡࡖࡵࡹࡪ࠲ࠠࡴࡷࡳࡴࡷ࡫ࡳࡴࡧࡶࠤࡵࡸࡩ࡯ࡶࠣࡳࡺࡺࡰࡶࡶ࠱ࠤࡉ࡫ࡦࡢࡷ࡯ࡸࠥࡌࡡ࡭ࡵࡨ࠲ࠏࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡪࡩࡤࡶ࠽ࠤࡈࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࡴࡨࡷࡺࡲࡴࡴࠢࡺ࡭ࡹ࡮ࠠ࡬ࡧࡼࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡳࡶࡥࡦࡩࡸࡹࠠࠩࡤࡲࡳࡱ࠯࠺࡙ࠡ࡫ࡩࡹ࡮ࡥࡳࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࠦࡳࡶࡥࡦࡩࡪࡪࡥࡥࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡦࡳࡺࡴࡴࠡࠪ࡬ࡲࡹ࠯࠺ࠡࡐࡸࡱࡧ࡫ࡲࠡࡱࡩࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡲ࡬ࡦࡥࡷࡩࡩࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦ࡮ࡰࡦࡨ࡭ࡩࡹࠠࠩ࡮࡬ࡷࡹ࠯࠺ࠡࡎ࡬ࡷࡹࠦ࡯ࡧࠢࡷࡩࡸࡺࠠ࡯ࡱࡧࡩࠥࡏࡄࡴࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡸࠦࠨ࡭࡫ࡶࡸ࠮ࡀࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡷࡱ࡭ࡶࡻࡥࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࠤࡵࡧࡴࡩࡵࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡩࡷࡸ࡯ࡳࠢࠫࡷࡹࡸࠩ࠻ࠢࡈࡶࡷࡵࡲࠡ࡯ࡨࡷࡸࡧࡧࡦࠢ࡬ࡪࠥࡹࡵࡤࡥࡨࡷࡸࠦࡩࡴࠢࡉࡥࡱࡹࡥࠋࠢࠣࠤࠥࡋࡸࡢ࡯ࡳࡰࡪࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡁࡂࡃࠦࠣࠡࡅࡲࡰࡱ࡫ࡣࡵࠢࡩࡶࡴࡳࠠࡵࡧࡶࡸࠥࡶࡡࡵࡪࡶࠎࠥࠦࠠࠡࠢࠣࠤࠥࡄ࠾࠿ࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡁࠥࡩ࡯࡭࡮ࡨࡧࡹࡥࡴࡦࡵࡷࡷࡤࡽࡩࡵࡪࡢࡴࡾࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࠪࡷࡩࡸࡺ࡟ࡱࡣࡷ࡬ࡸࡃ࡛ࠣࡶࡨࡷࡹࡹ࠯ࠣ࡟ࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥࡄ࠾࠿ࠢࡳࡶ࡮ࡴࡴࠩࡨࠥࡊࡴࡻ࡮ࡥࠢࡾࡶࡪࡹࡵ࡭ࡶࡶ࡟ࠬࡩ࡯ࡶࡰࡷࠫࡢࢃࠠࡵࡧࡶࡸࡸࠨࠩࠋࠢࠣࠤࠥࠦࠠࠡࠢࡁࡂࡃࠦࠣࠡࡅࡲࡰࡱ࡫ࡣࡵࠢࡺ࡭ࡹ࡮ࠠࡱࡻࡷࡩࡸࡺࠠࡢࡴࡪࡷࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠾࠿ࡀࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡂࠦࡣࡰ࡮࡯ࡩࡨࡺ࡟ࡵࡧࡶࡸࡸࡥࡷࡪࡶ࡫ࡣࡵࡿࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࠫࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠴࠮࠯ࠢࠣࠤࠥࠦࡴࡦࡵࡷࡣࡦࡸࡧࡴ࠿࡞ࠦࡹ࡫ࡳࡵࡵ࠲ࠦ࠱ࠦࠢ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠤ࠯ࠤࠧࡩࡨࡳࡱࡰࡩࠧࡣࠬࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠱࠲࠳ࠦࠠࠡࠢࠣࡷ࡮ࡲࡥ࡯ࡶࡀࡘࡷࡻࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠱࠲࠳ࠦࠩࠋࠢࠣࠤࠥࠨࠢࠣॆ")
    try:
        import pytest
        if bstack11ll11l1_opy_ is not None:
            args = list(bstack11ll11l1_opy_)
        elif bstack11l1lll1_opy_ is not None:
            if isinstance(bstack11l1lll1_opy_, str):
                args = [bstack11l1lll1_opy_]
            elif isinstance(bstack11l1lll1_opy_, list):
                args = list(bstack11l1lll1_opy_)
            else:
                args = [bstack11l1l11_opy_ (u"ࠤ࠱ࠦे")]
        else:
            args = [bstack11l1l11_opy_ (u"ࠥ࠲ࠧै")]
        bstack11ll1ll1_opy_ = args + [
            bstack11l1l11_opy_ (u"ࠦ࠲࠳ࡣࡰ࡮࡯ࡩࡨࡺ࠭ࡰࡰ࡯ࡽࠧॉ"),
        ]
        class bstack11l1llll_opy_:
            bstack11l1l11_opy_ (u"ࠧࠨࠢࡑࡻࡷࡩࡸࡺࠠࡱ࡮ࡸ࡫࡮ࡴࠠࡵࡪࡤࡸࠥࡩࡡࡱࡶࡸࡶࡪࡹࠠࡤࡱ࡯ࡰࡪࡩࡴࡦࡦࠣࡸࡪࡹࡴࠡ࡫ࡷࡩࡲࡹ࠮ࠣࠤࠥॊ")
            def __init__(self):
                self.bstack11ll1lll_opy_ = []
                self.test_files = set()
                self.bstack11ll111l_opy_ = None
            def pytest_collection_finish(self, session):
                bstack11l1l11_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡍࡵ࡯࡬ࠢࡦࡥࡱࡲࡥࡥࠢࡤࡪࡹ࡫ࡲࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡯ࡳࠡࡨ࡬ࡲ࡮ࡹࡨࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡃࡢࡲࡷࡹࡷ࡫ࡳࠡࡣ࡯ࡰࠥࡩ࡯࡭࡮ࡨࡧࡹ࡫ࡤࠡࡶࡨࡷࡹࠦࡩࡵࡧࡰࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦो")
                try:
                    for item in session.items:
                        nodeid = item.nodeid
                        self.bstack11ll1lll_opy_.append(nodeid)
                        if bstack11l1l11_opy_ (u"ࠢ࠻࠼ࠥौ") in nodeid:
                            file_path = nodeid.split(bstack11l1l11_opy_ (u"ࠣ࠼࠽्ࠦ"), 1)[0]
                            file_path = os.path.normpath(file_path).replace(bstack11l1l11_opy_ (u"ࠩ࡟ࡠࠬॎ"), bstack11l1l11_opy_ (u"ࠪ࠳ࠬॏ"))
                            if file_path.endswith(bstack11l1l11_opy_ (u"ࠫ࠳ࡶࡹࠨॐ")):
                                self.test_files.add(file_path)
                except Exception as e:
                    self.bstack11ll111l_opy_ = str(e)
        collector = bstack11l1llll_opy_()
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            exit_code = pytest.main(bstack11ll1ll1_opy_, plugins=[collector])
        if collector.bstack11ll111l_opy_:
            return {
                bstack11l1l11_opy_ (u"ࠧࡹࡵࡤࡥࡨࡷࡸࠨ॑"): False,
                bstack11l1l11_opy_ (u"ࠨࡣࡰࡷࡱࡸ॒ࠧ"): 0,
                bstack11l1l11_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࡳࠣ॓"): [],
                bstack11l1l11_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠧ॔"): [],
                bstack11l1l11_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣॕ"): bstack11l1l11_opy_ (u"ࠥࡇࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴࠠࡦࡴࡵࡳࡷࡀࠠࡼࡿࠥॖ").format(collector.bstack11ll111l_opy_)
            }
        return {
            bstack11l1l11_opy_ (u"ࠦࡸࡻࡣࡤࡧࡶࡷࠧॗ"): True,
            bstack11l1l11_opy_ (u"ࠧࡩ࡯ࡶࡰࡷࠦक़"): len(collector.bstack11ll1lll_opy_),
            bstack11l1l11_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࡹࠢख़"): collector.bstack11ll1lll_opy_,
            bstack11l1l11_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡶࠦग़"): sorted(collector.test_files),
            bstack11l1l11_opy_ (u"ࠣࡧࡻ࡭ࡹࡥࡣࡰࡦࡨࠦज़"): exit_code
        }
    except Exception as e:
        error_msg = bstack11l1l11_opy_ (u"ࠤࡘࡲࡪࡾࡰࡦࡥࡷࡩࡩࠦࡥࡳࡴࡲࡶࠥ࡯࡮ࠡࡶࡨࡷࡹࠦࡣࡰ࡮࡯ࡩࡨࡺࡩࡰࡰ࠽ࠤࢀࢃࠢड़").format(str(e))
        return {
            bstack11l1l11_opy_ (u"ࠥࡷࡺࡩࡣࡦࡵࡶࠦढ़"): False,
            bstack11l1l11_opy_ (u"ࠦࡨࡵࡵ࡯ࡶࠥफ़"): 0,
            bstack11l1l11_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࡸࠨय़"): [],
            bstack11l1l11_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯࡬ࡦࡵࠥॠ"): [],
            bstack11l1l11_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨॡ"): error_msg
        }
def bstack11l1ll1l_opy_(cache_dir=bstack11l1l11_opy_ (u"ࠨ࠰ࡳࡽࡹ࡫ࡳࡵࡡࡦࡥࡨ࡮ࡥࠨॢ")):
    bstack11l1l11_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡊࡩࡹࠦࡴࡩࡧࠣࡰ࡮ࡹࡴࠡࡱࡩࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࠢࡱࡳࡩ࡫ࠠࡊࡆࡶࠤࡩ࡯ࡲࡦࡥࡷࡰࡾࠦࡦࡳࡱࡰࠤࡵࡿࡴࡦࡵࡷࠤࡨࡧࡣࡩࡧ࠱ࠎࠥࠦࠠࠡࡖ࡫࡭ࡸࠦࡩࡴࠢࡩࡥࡸࡺࡥࡳࠢࡷ࡬ࡦࡴࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥࡧ࡮ࡥࠢࡦࡥࡳࠦࡢࡦࠢࡸࡷࡪࡪࠠࡵࡱࠣࡵࡺ࡯ࡣ࡬࡮ࡼࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠊࠡࠢࠣࠤࡼ࡮ࡩࡤࡪࠣࡸࡪࡹࡴࡴࠢࡩࡥ࡮ࡲࡥࡥࠢࡺ࡭ࡹ࡮࡯ࡶࡶࠣ࡭ࡳࡼ࡯࡬࡫ࡱ࡫ࠥࡶࡹࡵࡧࡶࡸ࠳ࠐࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡧࡦࡩࡨࡦࡡࡧ࡭ࡷࠦࠨࡴࡶࡵ࠭࠿ࠦࡐࡢࡶ࡫ࠤࡹࡵࠠࡱࡻࡷࡩࡸࡺࠠࡤࡣࡦ࡬ࡪࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺ࠰ࠣࡈࡪ࡬ࡡࡶ࡮ࡷࠤࠬ࠴ࡰࡺࡶࡨࡷࡹࡥࡣࡢࡥ࡫ࡩࠬࠐࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦ࡬ࡪࡵࡷ࠾ࠥࡒࡩࡴࡶࠣࡳ࡫ࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࠤࡳࡵࡤࡦࠢࡌࡈࡸ࠲ࠠࡰࡴࠣࡩࡲࡶࡴࡺࠢ࡯࡭ࡸࡺࠠࡪࡨࠣࡲࡴࠦࡦࡢ࡫࡯ࡹࡷ࡫ࡳࠡࡥࡤࡧ࡭࡫ࡤࠋࠢࠣࠤࠥࡋࡸࡢ࡯ࡳࡰࡪࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࡀࡁࡂࠥࠩࠠࡒࡷ࡬ࡧࡰࠦࡣࡩࡧࡦ࡯ࠥࡵࡦࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹࠠࡧࡴࡲࡱࠥࡩࡡࡤࡪࡨࠎࠥࠦࠠࠡࠢࠣࠤࠥࡄ࠾࠿ࠢࡩࡥ࡮ࡲࡥࡥࡡࡱࡳࡩ࡫ࡩࡥࡵࠣࡁࠥ࡭ࡥࡵࡡࡦࡥࡨ࡮ࡥࡥࡡࡩࡥ࡮ࡲࡥࡥࡡࡱࡳࡩ࡫ࡩࡥࡵࠫ࠭ࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠾࠿ࡀࠣࡴࡷ࡯࡮ࡵࠪࡩࠦࡕࡸࡥࡷ࡫ࡲࡹࡸࡲࡹࠡࡨࡤ࡭ࡱ࡫ࡤ࠻ࠢࡾࡰࡪࡴࠨࡧࡣ࡬ࡰࡪࡪ࡟࡯ࡱࡧࡩ࡮ࡪࡳࠪࡿࠣࡸࡪࡹࡴࡴࠤࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥࡄ࠾࠿ࠢࡩࡳࡷࠦ࡮ࡰࡦࡨ࡭ࡩࠦࡩ࡯ࠢࡩࡥ࡮ࡲࡥࡥࡡࡱࡳࡩ࡫ࡩࡥࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠴࠮࠯ࠢࠣࠤࠥࠦࡰࡳ࡫ࡱࡸ࠭࡬ࠢࠡࠢ࠰ࠤࢀࡴ࡯ࡥࡧ࡬ࡨࢂࠨࠩࠋࠢࠣࠤࠥࠨࠢࠣॣ")
    import json
    bstack11ll1l11_opy_ = os.path.join(cache_dir, bstack11l1l11_opy_ (u"ࠪࡺࠬ।"), bstack11l1l11_opy_ (u"ࠫࡨࡧࡣࡩࡧࠪ॥"), bstack11l1l11_opy_ (u"ࠬࡲࡡࡴࡶࡩࡥ࡮ࡲࡥࡥࠩ०"))
    try:
        if os.path.exists(bstack11ll1l11_opy_):
            with open(bstack11ll1l11_opy_, bstack11l1l11_opy_ (u"࠭ࡲࠨ१")) as f:
                bstack11l1ll11_opy_ = json.load(f)
                return list(bstack11l1ll11_opy_.keys())
        return []
    except Exception:
        return []