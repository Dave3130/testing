# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
bstack11ll_opy_ (u"ࠢࠣࠤࠍࡔࡾࡺࡥࡴࡶࠣࡸࡪࡹࡴࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡮ࡥ࡭ࡲࡨࡶࠥࡻࡳࡪࡰࡪࠤࡩ࡯ࡲࡦࡥࡷࠤࡵࡿࡴࡦࡵࡷࠤ࡭ࡵ࡯࡬ࡵ࠱ࠎࠧࠨࠢॅ")
import sys
import io
import os
from contextlib import redirect_stdout, redirect_stderr
def bstack11l1ll11_opy_(bstack11ll1l1l_opy_=None, bstack11l1lll1_opy_=None, bstack11ll11ll_opy_=False, bstack11ll1lll_opy_=False):
    bstack11ll_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡅࡲࡰࡱ࡫ࡣࡵࠢࡳࡽࡹ࡫ࡳࡵࠢࡷࡩࡸࡺࡳࠡࡷࡶ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠧࡴࠢ࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠤࡆࡖࡉࡴ࠰ࠍࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡵࡧࡶࡸࡤࡧࡲࡨࡵࠣࠬࡱ࡯ࡳࡵ࠮ࠣࡳࡵࡺࡩࡰࡰࡤࡰ࠮ࡀࠠࡄࡱࡰࡴࡱ࡫ࡴࡦࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡴࡾࡺࡥࡴࡶࠣࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠦࡩ࡯ࡥ࡯ࡹࡩ࡯࡮ࡨࠢࡳࡥࡹ࡮ࡳࠡࡣࡱࡨࠥ࡬࡬ࡢࡩࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡡ࡬ࡧࡶࠤࡵࡸࡥࡤࡧࡧࡩࡳࡩࡥࠡࡱࡹࡩࡷࠦࡴࡦࡵࡷࡣࡵࡧࡴࡩࡵࠣ࡭࡫ࠦࡢࡰࡶ࡫ࠤࡦࡸࡥࠡࡲࡵࡳࡻ࡯ࡤࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡺࡥࡴࡶࡢࡴࡦࡺࡨࡴࠢࠫࡰ࡮ࡹࡴࠡࡱࡵࠤࡸࡺࡲ࠭ࠢࡲࡴࡹ࡯࡯࡯ࡣ࡯࠭࠿ࠦࡔࡦࡵࡷࠤ࡫࡯࡬ࡦࠪࡶ࠭࠴ࡪࡩࡳࡧࡦࡸࡴࡸࡹࠩ࡫ࡨࡷ࠮ࠦࡴࡰࠢࡦࡳࡱࡲࡥࡤࡶࠣࡪࡷࡵ࡭࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡇࡦࡴࠠࡣࡧࠣࡥࠥࡹࡩ࡯ࡩ࡯ࡩࠥࡶࡡࡵࡪࠣࡷࡹࡸࡩ࡯ࡩࠣࡳࡷࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡱࡣࡷ࡬ࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡋࡪࡲࡴࡸࡥࡥࠢ࡬ࡪࠥࡺࡥࡴࡶࡢࡥࡷ࡭ࡳࠡ࡫ࡶࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡵ࡬ࡰࡪࡴࡴࠡࠪࡥࡳࡴࡲࠬࠡࡱࡳࡸ࡮ࡵ࡮ࡢ࡮ࠬ࠾ࠥࡏࡦࠡࡖࡵࡹࡪ࠲ࠠࡴࡷࡳࡴࡷ࡫ࡳࡴࡧࡶࠤࡵࡸࡩ࡯ࡶࠣࡳࡺࡺࡰࡶࡶ࠱ࠤࡉ࡫ࡦࡢࡷ࡯ࡸࠥࡌࡡ࡭ࡵࡨ࠲ࠏࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡪࡩࡤࡶ࠽ࠤࡈࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࡴࡨࡷࡺࡲࡴࡴࠢࡺ࡭ࡹ࡮ࠠ࡬ࡧࡼࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡳࡶࡥࡦࡩࡸࡹࠠࠩࡤࡲࡳࡱ࠯࠺࡙ࠡ࡫ࡩࡹ࡮ࡥࡳࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࠦࡳࡶࡥࡦࡩࡪࡪࡥࡥࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡦࡳࡺࡴࡴࠡࠪ࡬ࡲࡹ࠯࠺ࠡࡐࡸࡱࡧ࡫ࡲࠡࡱࡩࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡲ࡬ࡦࡥࡷࡩࡩࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦ࡮ࡰࡦࡨ࡭ࡩࡹࠠࠩ࡮࡬ࡷࡹ࠯࠺ࠡࡎ࡬ࡷࡹࠦ࡯ࡧࠢࡷࡩࡸࡺࠠ࡯ࡱࡧࡩࠥࡏࡄࡴࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡸࠦࠨ࡭࡫ࡶࡸ࠮ࡀࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡷࡱ࡭ࡶࡻࡥࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࠤࡵࡧࡴࡩࡵࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡩࡷࡸ࡯ࡳࠢࠫࡷࡹࡸࠩ࠻ࠢࡈࡶࡷࡵࡲࠡ࡯ࡨࡷࡸࡧࡧࡦࠢ࡬ࡪࠥࡹࡵࡤࡥࡨࡷࡸࠦࡩࡴࠢࡉࡥࡱࡹࡥࠋࠢࠣࠤࠥࡋࡸࡢ࡯ࡳࡰࡪࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡁࡂࡃࠦࠣࠡࡅࡲࡰࡱ࡫ࡣࡵࠢࡩࡶࡴࡳࠠࡵࡧࡶࡸࠥࡶࡡࡵࡪࡶࠎࠥࠦࠠࠡࠢࠣࠤࠥࡄ࠾࠿ࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡁࠥࡩ࡯࡭࡮ࡨࡧࡹࡥࡴࡦࡵࡷࡷࡤࡽࡩࡵࡪࡢࡴࡾࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࠪࡷࡩࡸࡺ࡟ࡱࡣࡷ࡬ࡸࡃ࡛ࠣࡶࡨࡷࡹࡹ࠯ࠣ࡟ࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥࡄ࠾࠿ࠢࡳࡶ࡮ࡴࡴࠩࡨࠥࡊࡴࡻ࡮ࡥࠢࡾࡶࡪࡹࡵ࡭ࡶࡶ࡟ࠬࡩ࡯ࡶࡰࡷࠫࡢࢃࠠࡵࡧࡶࡸࡸࠨࠩࠋࠢࠣࠤࠥࠦࠠࠡࠢࡁࡂࡃࠦࠣࠡࡅࡲࡰࡱ࡫ࡣࡵࠢࡺ࡭ࡹ࡮ࠠࡱࡻࡷࡩࡸࡺࠠࡢࡴࡪࡷࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠾࠿ࡀࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡂࠦࡣࡰ࡮࡯ࡩࡨࡺ࡟ࡵࡧࡶࡸࡸࡥࡷࡪࡶ࡫ࡣࡵࡿࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࠫࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠴࠮࠯ࠢࠣࠤࠥࠦࡴࡦࡵࡷࡣࡦࡸࡧࡴ࠿࡞ࠦࡹ࡫ࡳࡵࡵ࠲ࠦ࠱ࠦࠢ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠤ࠯ࠤࠧࡩࡨࡳࡱࡰࡩࠧࡣࠬࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠱࠲࠳ࠦࠠࠡࠢࠣࡷ࡮ࡲࡥ࡯ࡶࡀࡘࡷࡻࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠱࠲࠳ࠦࠩࠋࠢࠣࠤࠥࠨࠢࠣॆ")
    try:
        import pytest
        if bstack11ll1l1l_opy_ is not None:
            args = list(bstack11ll1l1l_opy_)
        elif bstack11l1lll1_opy_ is not None:
            if isinstance(bstack11l1lll1_opy_, str):
                args = [bstack11l1lll1_opy_]
            elif isinstance(bstack11l1lll1_opy_, list):
                args = list(bstack11l1lll1_opy_)
            else:
                args = [bstack11ll_opy_ (u"ࠤ࠱ࠦे")]
        else:
            args = [bstack11ll_opy_ (u"ࠥ࠲ࠧै")]
        bstack11l1l1l1_opy_ = args + [
            bstack11ll_opy_ (u"ࠦ࠲࠳ࡣࡰ࡮࡯ࡩࡨࡺ࠭ࡰࡰ࡯ࡽࠧॉ"),
        ]
        if bstack11ll11ll_opy_:
            bstack11l1l1l1_opy_.append(bstack11ll_opy_ (u"ࠧ࠳ࡱࠣॊ"))
        if not bstack11ll1lll_opy_:
            bstack11l1l1l1_opy_.extend([bstack11ll_opy_ (u"ࠨ࠭ࡱࠤो"), bstack11ll_opy_ (u"ࠢ࡯ࡱ࠽ࡧࡦࡩࡨࡦࡲࡵࡳࡻ࡯ࡤࡦࡴࠥौ")])
        class bstack11l1ll1l_opy_:
            bstack11ll_opy_ (u"ࠣࠤࠥࡔࡾࡺࡥࡴࡶࠣࡴࡱࡻࡧࡪࡰࠣࡸ࡭ࡧࡴࠡࡥࡤࡴࡹࡻࡲࡦࡵࠣࡧࡴࡲ࡬ࡦࡥࡷࡩࡩࠦࡴࡦࡵࡷࠤ࡮ࡺࡥ࡮ࡵ࠱ࠦࠧࠨ्")
            def __init__(self):
                self.bstack11l1l1ll_opy_ = []
                self.test_files = set()
                self.bstack11ll1111_opy_ = None
            def pytest_collection_finish(self, session):
                bstack11ll_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡉࡱࡲ࡯ࠥࡩࡡ࡭࡮ࡨࡨࠥࡧࡦࡵࡧࡵࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮ࠡ࡫ࡶࠤ࡫࡯࡮ࡪࡵ࡫ࡩࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡆࡥࡵࡺࡵࡳࡧࡶࠤࡦࡲ࡬ࠡࡥࡲࡰࡱ࡫ࡣࡵࡧࡧࠤࡹ࡫ࡳࡵࠢ࡬ࡸࡪࡳࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢॎ")
                try:
                    for item in session.items:
                        nodeid = item.nodeid
                        self.bstack11l1l1ll_opy_.append(nodeid)
                        if bstack11ll_opy_ (u"ࠥ࠾࠿ࠨॏ") in nodeid:
                            file_path = nodeid.split(bstack11ll_opy_ (u"ࠦ࠿ࡀࠢॐ"), 1)[0]
                            file_path = os.path.normpath(file_path).replace(bstack11ll_opy_ (u"ࠬࡢ࡜ࠨ॑"), bstack11ll_opy_ (u"࠭࠯ࠨ॒"))
                            if file_path.endswith(bstack11ll_opy_ (u"ࠧ࠯ࡲࡼࠫ॓")):
                                self.test_files.add(file_path)
                except Exception as e:
                    self.bstack11ll1111_opy_ = str(e)
        collector = bstack11l1ll1l_opy_()
        if bstack11ll11ll_opy_:
            with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                exit_code = pytest.main(bstack11l1l1l1_opy_, plugins=[collector])
        else:
            exit_code = pytest.main(bstack11l1l1l1_opy_, plugins=[collector])
        if collector.bstack11ll1111_opy_:
            return {
                bstack11ll_opy_ (u"ࠣࡵࡸࡧࡨ࡫ࡳࡴࠤ॔"): False,
                bstack11ll_opy_ (u"ࠤࡦࡳࡺࡴࡴࠣॕ"): 0,
                bstack11ll_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࡶࠦॖ"): [],
                bstack11ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡩ࡭ࡱ࡫ࡳࠣॗ"): [],
                bstack11ll_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦक़"): bstack11l1llll_opy_ (u"ࠨࡃࡰ࡮࡯ࡩࡨࡺࡩࡰࡰࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࡨࡵ࡬࡭ࡧࡦࡸࡴࡸ࠮ࡤࡱ࡯ࡰࡪࡩࡴࡪࡱࡱࡣࡪࡸࡲࡰࡴࢀࠦख़")
            }
        return {
            bstack11ll_opy_ (u"ࠢࡴࡷࡦࡧࡪࡹࡳࠣग़"): True,
            bstack11ll_opy_ (u"ࠣࡥࡲࡹࡳࡺࠢज़"): len(collector.bstack11l1l1ll_opy_),
            bstack11ll_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࡵࠥड़"): collector.bstack11l1l1ll_opy_,
            bstack11ll_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨ࡬ࡰࡪࡹࠢढ़"): sorted(collector.test_files),
            bstack11ll_opy_ (u"ࠦࡪࡾࡩࡵࡡࡦࡳࡩ࡫ࠢफ़"): exit_code
        }
    except Exception as e:
        error_msg = bstack11l1llll_opy_ (u"࡛ࠧ࡮ࡦࡺࡳࡩࡨࡺࡥࡥࠢࡨࡶࡷࡵࡲࠡ࡫ࡱࠤࡹ࡫ࡳࡵࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࡀࠠࡼࡵࡷࡶ࠭࡫ࠩࡾࠤय़")
        return {
            bstack11ll_opy_ (u"ࠨࡳࡶࡥࡦࡩࡸࡹࠢॠ"): False,
            bstack11ll_opy_ (u"ࠢࡤࡱࡸࡲࡹࠨॡ"): 0,
            bstack11ll_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࡴࠤॢ"): [],
            bstack11ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡸࠨॣ"): [],
            bstack11ll_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤ।"): error_msg
        }
def bstack11ll1ll1_opy_(cache_dir=bstack11ll_opy_ (u"ࠫ࠳ࡶࡹࡵࡧࡶࡸࡤࡩࡡࡤࡪࡨࠫ॥")):
    bstack11ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡍࡥࡵࠢࡷ࡬ࡪࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࠥࡴ࡯ࡥࡧࠣࡍࡉࡹࠠࡥ࡫ࡵࡩࡨࡺ࡬ࡺࠢࡩࡶࡴࡳࠠࡱࡻࡷࡩࡸࡺࠠࡤࡣࡦ࡬ࡪ࠴ࠊࠡࠢࠣࠤ࡙࡮ࡩࡴࠢ࡬ࡷࠥ࡬ࡡࡴࡶࡨࡶࠥࡺࡨࡢࡰࠣࡶࡺࡴ࡮ࡪࡰࡪࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࡣࡱࡨࠥࡩࡡ࡯ࠢࡥࡩࠥࡻࡳࡦࡦࠣࡸࡴࠦࡱࡶ࡫ࡦ࡯ࡱࡿࠠࡥࡧࡷࡩࡷࡳࡩ࡯ࡧࠍࠤࠥࠦࠠࡸࡪ࡬ࡧ࡭ࠦࡴࡦࡵࡷࡷࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪࡲࡹࡹࠦࡩ࡯ࡸࡲ࡯࡮ࡴࡧࠡࡲࡼࡸࡪࡹࡴ࠯ࠌࠣࠤࠥࠦࡁࡳࡩࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡣࡢࡥ࡫ࡩࡤࡪࡩࡳࠢࠫࡷࡹࡸࠩ࠻ࠢࡓࡥࡹ࡮ࠠࡵࡱࠣࡴࡾࡺࡥࡴࡶࠣࡧࡦࡩࡨࡦࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽ࠳ࠦࡄࡦࡨࡤࡹࡱࡺࠠࠨ࠰ࡳࡽࡹ࡫ࡳࡵࡡࡦࡥࡨ࡮ࡥࠨࠌࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡯࡭ࡸࡺ࠺ࠡࡎ࡬ࡷࡹࠦ࡯ࡧࠢࡩࡥ࡮ࡲࡥࡥࠢࡷࡩࡸࡺࠠ࡯ࡱࡧࡩࠥࡏࡄࡴ࠮ࠣࡳࡷࠦࡥ࡮ࡲࡷࡽࠥࡲࡩࡴࡶࠣ࡭࡫ࠦ࡮ࡰࠢࡩࡥ࡮ࡲࡵࡳࡧࡶࠤࡨࡧࡣࡩࡧࡧࠎࠥࠦࠠࠡࡇࡻࡥࡲࡶ࡬ࡦ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡃࡄ࠾ࠡࠥࠣࡕࡺ࡯ࡣ࡬ࠢࡦ࡬ࡪࡩ࡫ࠡࡱࡩࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࡵࠣࡪࡷࡵ࡭ࠡࡥࡤࡧ࡭࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡀࡁࡂࠥ࡬ࡡࡪ࡮ࡨࡨࡤࡴ࡯ࡥࡧ࡬ࡨࡸࠦ࠽ࠡࡩࡨࡸࡤࡩࡡࡤࡪࡨࡨࡤ࡬ࡡࡪ࡮ࡨࡨࡤࡴ࡯ࡥࡧ࡬ࡨࡸ࠮ࠩࠋࠢࠣࠤࠥࠦࠠࠡࠢࡁࡂࡃࠦࡰࡳ࡫ࡱࡸ࠭࡬ࠢࡑࡴࡨࡺ࡮ࡵࡵࡴ࡮ࡼࠤ࡫ࡧࡩ࡭ࡧࡧ࠾ࠥࢁ࡬ࡦࡰࠫࡪࡦ࡯࡬ࡦࡦࡢࡲࡴࡪࡥࡪࡦࡶ࠭ࢂࠦࡴࡦࡵࡷࡷࠧ࠯ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡀࡁࡂࠥ࡬࡯ࡳࠢࡱࡳࡩ࡫ࡩࡥࠢ࡬ࡲࠥ࡬ࡡࡪ࡮ࡨࡨࡤࡴ࡯ࡥࡧ࡬ࡨࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠰࠱࠲ࠥࠦࠠࠡࠢࡳࡶ࡮ࡴࡴࠩࡨࠥࠤࠥ࠳ࠠࡼࡰࡲࡨࡪ࡯ࡤࡾࠤࠬࠎࠥࠦࠠࠡࠤࠥࠦ०")
    import json
    bstack11ll1l11_opy_ = os.path.join(cache_dir, bstack11ll_opy_ (u"࠭ࡶࠨ१"), bstack11ll_opy_ (u"ࠧࡤࡣࡦ࡬ࡪ࠭२"), bstack11ll_opy_ (u"ࠨ࡮ࡤࡷࡹ࡬ࡡࡪ࡮ࡨࡨࠬ३"))
    try:
        if os.path.exists(bstack11ll1l11_opy_):
            with open(bstack11ll1l11_opy_, bstack11ll_opy_ (u"ࠩࡵࠫ४")) as f:
                bstack11ll111l_opy_ = json.load(f)
                return list(bstack11ll111l_opy_.keys())
        return []
    except Exception:
        return []