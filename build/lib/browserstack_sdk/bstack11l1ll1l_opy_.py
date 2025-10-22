# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
bstack1l111ll_opy_ (u"ࠢࠣࠤࠍࡔࡾࡺࡥࡴࡶࠣࡸࡪࡹࡴࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡮ࡥ࡭ࡲࡨࡶࠥࡻࡳࡪࡰࡪࠤࡩ࡯ࡲࡦࡥࡷࠤࡵࡿࡴࡦࡵࡷࠤ࡭ࡵ࡯࡬ࡵ࠱ࠎࠧࠨࠢॅ")
import sys
import io
import os
from contextlib import redirect_stdout, redirect_stderr
def bstack11l1lll1_opy_(bstack11ll1lll_opy_=None, bstack11ll11ll_opy_=None, bstack11ll1111_opy_=False):
    bstack1l111ll_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡅࡲࡰࡱ࡫ࡣࡵࠢࡳࡽࡹ࡫ࡳࡵࠢࡷࡩࡸࡺࡳࠡࡷࡶ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠧࡴࠢ࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠤࡆࡖࡉࡴ࠰ࠍࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡵࡧࡶࡸࡤࡧࡲࡨࡵࠣࠬࡱ࡯ࡳࡵ࠮ࠣࡳࡵࡺࡩࡰࡰࡤࡰ࠮ࡀࠠࡄࡱࡰࡴࡱ࡫ࡴࡦࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡴࡾࡺࡥࡴࡶࠣࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠦࡩ࡯ࡥ࡯ࡹࡩ࡯࡮ࡨࠢࡳࡥࡹ࡮ࡳࠡࡣࡱࡨࠥ࡬࡬ࡢࡩࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡡ࡬ࡧࡶࠤࡵࡸࡥࡤࡧࡧࡩࡳࡩࡥࠡࡱࡹࡩࡷࠦࡴࡦࡵࡷࡣࡵࡧࡴࡩࡵࠣ࡭࡫ࠦࡢࡰࡶ࡫ࠤࡦࡸࡥࠡࡲࡵࡳࡻ࡯ࡤࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡺࡥࡴࡶࡢࡴࡦࡺࡨࡴࠢࠫࡰ࡮ࡹࡴࠡࡱࡵࠤࡸࡺࡲ࠭ࠢࡲࡴࡹ࡯࡯࡯ࡣ࡯࠭࠿ࠦࡔࡦࡵࡷࠤ࡫࡯࡬ࡦࠪࡶ࠭࠴ࡪࡩࡳࡧࡦࡸࡴࡸࡹࠩ࡫ࡨࡷ࠮ࠦࡴࡰࠢࡦࡳࡱࡲࡥࡤࡶࠣࡪࡷࡵ࡭࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡇࡦࡴࠠࡣࡧࠣࡥࠥࡹࡩ࡯ࡩ࡯ࡩࠥࡶࡡࡵࡪࠣࡷࡹࡸࡩ࡯ࡩࠣࡳࡷࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡱࡣࡷ࡬ࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡋࡪࡲࡴࡸࡥࡥࠢ࡬ࡪࠥࡺࡥࡴࡶࡢࡥࡷ࡭ࡳࠡ࡫ࡶࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡵ࡬ࡰࡪࡴࡴࠡࠪࡥࡳࡴࡲࠬࠡࡱࡳࡸ࡮ࡵ࡮ࡢ࡮ࠬ࠾ࠥࡏࡦࠡࡖࡵࡹࡪ࠲ࠠࡴࡷࡳࡴࡷ࡫ࡳࡴࡧࡶࠤࡵࡸࡩ࡯ࡶࠣࡳࡺࡺࡰࡶࡶ࠱ࠤࡉ࡫ࡦࡢࡷ࡯ࡸࠥࡌࡡ࡭ࡵࡨ࠲ࠏࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡪࡩࡤࡶ࠽ࠤࡈࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࡴࡨࡷࡺࡲࡴࡴࠢࡺ࡭ࡹ࡮ࠠ࡬ࡧࡼࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡳࡶࡥࡦࡩࡸࡹࠠࠩࡤࡲࡳࡱ࠯࠺࡙ࠡ࡫ࡩࡹ࡮ࡥࡳࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࠦࡳࡶࡥࡦࡩࡪࡪࡥࡥࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡦࡳࡺࡴࡴࠡࠪ࡬ࡲࡹ࠯࠺ࠡࡐࡸࡱࡧ࡫ࡲࠡࡱࡩࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡲ࡬ࡦࡥࡷࡩࡩࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦ࡮ࡰࡦࡨ࡭ࡩࡹࠠࠩ࡮࡬ࡷࡹ࠯࠺ࠡࡎ࡬ࡷࡹࠦ࡯ࡧࠢࡷࡩࡸࡺࠠ࡯ࡱࡧࡩࠥࡏࡄࡴࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡸࠦࠨ࡭࡫ࡶࡸ࠮ࡀࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡷࡱ࡭ࡶࡻࡥࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࠤࡵࡧࡴࡩࡵࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡩࡷࡸ࡯ࡳࠢࠫࡷࡹࡸࠩ࠻ࠢࡈࡶࡷࡵࡲࠡ࡯ࡨࡷࡸࡧࡧࡦࠢ࡬ࡪࠥࡹࡵࡤࡥࡨࡷࡸࠦࡩࡴࠢࡉࡥࡱࡹࡥࠋࠢࠣࠤࠥࡋࡸࡢ࡯ࡳࡰࡪࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡁࡂࡃࠦࠣࠡࡅࡲࡰࡱ࡫ࡣࡵࠢࡩࡶࡴࡳࠠࡵࡧࡶࡸࠥࡶࡡࡵࡪࡶࠎࠥࠦࠠࠡࠢࠣࠤࠥࡄ࠾࠿ࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡁࠥࡩ࡯࡭࡮ࡨࡧࡹࡥࡴࡦࡵࡷࡷࡤࡽࡩࡵࡪࡢࡴࡾࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࠪࡷࡩࡸࡺ࡟ࡱࡣࡷ࡬ࡸࡃ࡛ࠣࡶࡨࡷࡹࡹ࠯ࠣ࡟ࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥࡄ࠾࠿ࠢࡳࡶ࡮ࡴࡴࠩࡨࠥࡊࡴࡻ࡮ࡥࠢࡾࡶࡪࡹࡵ࡭ࡶࡶ࡟ࠬࡩ࡯ࡶࡰࡷࠫࡢࢃࠠࡵࡧࡶࡸࡸࠨࠩࠋࠢࠣࠤࠥࠦࠠࠡࠢࡁࡂࡃࠦࠣࠡࡅࡲࡰࡱ࡫ࡣࡵࠢࡺ࡭ࡹ࡮ࠠࡱࡻࡷࡩࡸࡺࠠࡢࡴࡪࡷࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠾࠿ࡀࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡂࠦࡣࡰ࡮࡯ࡩࡨࡺ࡟ࡵࡧࡶࡸࡸࡥࡷࡪࡶ࡫ࡣࡵࡿࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࠫࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠴࠮࠯ࠢࠣࠤࠥࠦࡴࡦࡵࡷࡣࡦࡸࡧࡴ࠿࡞ࠦࡹ࡫ࡳࡵࡵ࠲ࠦ࠱ࠦࠢ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠤ࠯ࠤࠧࡩࡨࡳࡱࡰࡩࠧࡣࠬࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠱࠲࠳ࠦࠠࠡࠢࠣࡷ࡮ࡲࡥ࡯ࡶࡀࡘࡷࡻࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠱࠲࠳ࠦࠩࠋࠢࠣࠤࠥࠨࠢࠣॆ")
    try:
        import pytest
        if bstack11ll1lll_opy_ is not None:
            args = list(bstack11ll1lll_opy_)
        elif bstack11ll11ll_opy_ is not None:
            if isinstance(bstack11ll11ll_opy_, str):
                args = [bstack11ll11ll_opy_]
            elif isinstance(bstack11ll11ll_opy_, list):
                args = list(bstack11ll11ll_opy_)
            else:
                args = [bstack1l111ll_opy_ (u"ࠤ࠱ࠦे")]
        else:
            args = [bstack1l111ll_opy_ (u"ࠥ࠲ࠧै")]
        bstack11ll1l1l_opy_ = args + [
            bstack1l111ll_opy_ (u"ࠦ࠲࠳ࡣࡰ࡮࡯ࡩࡨࡺ࠭ࡰࡰ࡯ࡽࠧॉ"),
        ]
        if bstack11ll1111_opy_:
            bstack11ll1l1l_opy_.append(bstack1l111ll_opy_ (u"ࠧ࠳ࡱࠣॊ"))
        class bstack11ll111l_opy_:
            bstack1l111ll_opy_ (u"ࠨࠢࠣࡒࡼࡸࡪࡹࡴࠡࡲ࡯ࡹ࡬࡯࡮ࠡࡶ࡫ࡥࡹࠦࡣࡢࡲࡷࡹࡷ࡫ࡳࠡࡥࡲࡰࡱ࡫ࡣࡵࡧࡧࠤࡹ࡫ࡳࡵࠢ࡬ࡸࡪࡳࡳ࠯ࠤࠥࠦो")
            def __init__(self):
                self.bstack11ll11l1_opy_ = []
                self.test_files = set()
                self.bstack11l1ll11_opy_ = None
            def pytest_collection_finish(self, session):
                bstack1l111ll_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡎ࡯ࡰ࡭ࠣࡧࡦࡲ࡬ࡦࡦࠣࡥ࡫ࡺࡥࡳࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࠦࡩࡴࠢࡩ࡭ࡳ࡯ࡳࡩࡧࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡄࡣࡳࡸࡺࡸࡥࡴࠢࡤࡰࡱࠦࡣࡰ࡮࡯ࡩࡨࡺࡥࡥࠢࡷࡩࡸࡺࠠࡪࡶࡨࡱࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧौ")
                try:
                    for item in session.items:
                        nodeid = item.nodeid
                        self.bstack11ll11l1_opy_.append(nodeid)
                        if bstack1l111ll_opy_ (u"ࠣ࠼࠽्ࠦ") in nodeid:
                            file_path = nodeid.split(bstack1l111ll_opy_ (u"ࠤ࠽࠾ࠧॎ"), 1)[0]
                            file_path = os.path.normpath(file_path).replace(bstack1l111ll_opy_ (u"ࠪࡠࡡ࠭ॏ"), bstack1l111ll_opy_ (u"ࠫ࠴࠭ॐ"))
                            if file_path.endswith(bstack1l111ll_opy_ (u"ࠬ࠴ࡰࡺࠩ॑")):
                                self.test_files.add(file_path)
                except Exception as e:
                    self.bstack11l1ll11_opy_ = str(e)
        collector = bstack11ll111l_opy_()
        if bstack11ll1111_opy_:
            with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                exit_code = pytest.main(bstack11ll1l1l_opy_, plugins=[collector])
        else:
            exit_code = pytest.main(bstack11ll1l1l_opy_, plugins=[collector])
        if collector.bstack11l1ll11_opy_:
            return {
                bstack1l111ll_opy_ (u"ࠨࡳࡶࡥࡦࡩࡸࡹ॒ࠢ"): False,
                bstack1l111ll_opy_ (u"ࠢࡤࡱࡸࡲࡹࠨ॓"): 0,
                bstack1l111ll_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࡴࠤ॔"): [],
                bstack1l111ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡸࠨॕ"): [],
                bstack1l111ll_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤॖ"): bstack1l111ll_opy_ (u"ࠦࡈࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠦॗ").format(collector.bstack11l1ll11_opy_)
            }
        return {
            bstack1l111ll_opy_ (u"ࠧࡹࡵࡤࡥࡨࡷࡸࠨक़"): True,
            bstack1l111ll_opy_ (u"ࠨࡣࡰࡷࡱࡸࠧख़"): len(collector.bstack11ll11l1_opy_),
            bstack1l111ll_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࡳࠣग़"): collector.bstack11ll11l1_opy_,
            bstack1l111ll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠧज़"): sorted(collector.test_files),
            bstack1l111ll_opy_ (u"ࠤࡨࡼ࡮ࡺ࡟ࡤࡱࡧࡩࠧड़"): exit_code
        }
    except Exception as e:
        error_msg = bstack1l111ll_opy_ (u"࡙ࠥࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡦࡴࡵࡳࡷࠦࡩ࡯ࠢࡷࡩࡸࡺࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡱࡱ࠾ࠥࢁࡽࠣढ़").format(str(e))
        return {
            bstack1l111ll_opy_ (u"ࠦࡸࡻࡣࡤࡧࡶࡷࠧफ़"): False,
            bstack1l111ll_opy_ (u"ࠧࡩ࡯ࡶࡰࡷࠦय़"): 0,
            bstack1l111ll_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࡹࠢॠ"): [],
            bstack1l111ll_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡶࠦॡ"): [],
            bstack1l111ll_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢॢ"): error_msg
        }
def bstack11ll1ll1_opy_(cache_dir=bstack1l111ll_opy_ (u"ࠩ࠱ࡴࡾࡺࡥࡴࡶࡢࡧࡦࡩࡨࡦࠩॣ")):
    bstack1l111ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡋࡪࡺࠠࡵࡪࡨࠤࡱ࡯ࡳࡵࠢࡲࡪࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࠣࡲࡴࡪࡥࠡࡋࡇࡷࠥࡪࡩࡳࡧࡦࡸࡱࡿࠠࡧࡴࡲࡱࠥࡶࡹࡵࡧࡶࡸࠥࡩࡡࡤࡪࡨ࠲ࠏࠦࠠࠡࠢࡗ࡬࡮ࡹࠠࡪࡵࠣࡪࡦࡹࡴࡦࡴࠣࡸ࡭ࡧ࡮ࠡࡴࡸࡲࡳ࡯࡮ࡨࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࠦࡡ࡯ࡦࠣࡧࡦࡴࠠࡣࡧࠣࡹࡸ࡫ࡤࠡࡶࡲࠤࡶࡻࡩࡤ࡭࡯ࡽࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠋࠢࠣࠤࠥࡽࡨࡪࡥ࡫ࠤࡹ࡫ࡳࡵࡵࠣࡪࡦ࡯࡬ࡦࡦࠣࡻ࡮ࡺࡨࡰࡷࡷࠤ࡮ࡴࡶࡰ࡭࡬ࡲ࡬ࠦࡰࡺࡶࡨࡷࡹ࠴ࠊࠡࠢࠣࠤࡆࡸࡧࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡨࡧࡣࡩࡧࡢࡨ࡮ࡸࠠࠩࡵࡷࡶ࠮ࡀࠠࡑࡣࡷ࡬ࠥࡺ࡯ࠡࡲࡼࡸࡪࡹࡴࠡࡥࡤࡧ࡭࡫ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻ࠱ࠤࡉ࡫ࡦࡢࡷ࡯ࡸࠥ࠭࠮ࡱࡻࡷࡩࡸࡺ࡟ࡤࡣࡦ࡬ࡪ࠭ࠊࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠ࡭࡫ࡶࡸ࠿ࠦࡌࡪࡵࡷࠤࡴ࡬ࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࠥࡴ࡯ࡥࡧࠣࡍࡉࡹࠬࠡࡱࡵࠤࡪࡳࡰࡵࡻࠣࡰ࡮ࡹࡴࠡ࡫ࡩࠤࡳࡵࠠࡧࡣ࡬ࡰࡺࡸࡥࡴࠢࡦࡥࡨ࡮ࡥࡥࠌࠣࠤࠥࠦࡅࡹࡣࡰࡴࡱ࡫࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡁࡂࡃࠦࠣࠡࡓࡸ࡭ࡨࡱࠠࡤࡪࡨࡧࡰࠦ࡯ࡧࠢࡩࡥ࡮ࡲࡥࡥࠢࡷࡩࡸࡺࡳࠡࡨࡵࡳࡲࠦࡣࡢࡥ࡫ࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠾࠿ࡀࠣࡪࡦ࡯࡬ࡦࡦࡢࡲࡴࡪࡥࡪࡦࡶࠤࡂࠦࡧࡦࡶࡢࡧࡦࡩࡨࡦࡦࡢࡪࡦ࡯࡬ࡦࡦࡢࡲࡴࡪࡥࡪࡦࡶࠬ࠮ࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠿ࡀࡁࠤࡵࡸࡩ࡯ࡶࠫࡪࠧࡖࡲࡦࡸ࡬ࡳࡺࡹ࡬ࡺࠢࡩࡥ࡮ࡲࡥࡥ࠼ࠣࡿࡱ࡫࡮ࠩࡨࡤ࡭ࡱ࡫ࡤࡠࡰࡲࡨࡪ࡯ࡤࡴࠫࢀࠤࡹ࡫ࡳࡵࡵࠥ࠭ࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠾࠿ࡀࠣࡪࡴࡸࠠ࡯ࡱࡧࡩ࡮ࡪࠠࡪࡰࠣࡪࡦ࡯࡬ࡦࡦࡢࡲࡴࡪࡥࡪࡦࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠮࠯࠰ࠣࠤࠥࠦࠠࡱࡴ࡬ࡲࡹ࠮ࡦࠣࠢࠣ࠱ࠥࢁ࡮ࡰࡦࡨ࡭ࡩࢃࠢࠪࠌࠣࠤࠥࠦࠢࠣࠤ।")
    import json
    bstack11l1llll_opy_ = os.path.join(cache_dir, bstack1l111ll_opy_ (u"ࠫࡻ࠭॥"), bstack1l111ll_opy_ (u"ࠬࡩࡡࡤࡪࡨࠫ०"), bstack1l111ll_opy_ (u"࠭࡬ࡢࡵࡷࡪࡦ࡯࡬ࡦࡦࠪ१"))
    try:
        if os.path.exists(bstack11l1llll_opy_):
            with open(bstack11l1llll_opy_, bstack1l111ll_opy_ (u"ࠧࡳࠩ२")) as f:
                bstack11ll1l11_opy_ = json.load(f)
                return list(bstack11ll1l11_opy_.keys())
        return []
    except Exception:
        return []