# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
bstack11ll1ll_opy_ (u"ࠢࠣࠤࠍࡔࡾࡺࡥࡴࡶࠣࡸࡪࡹࡴࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡮ࡥ࡭ࡲࡨࡶࠥࡻࡳࡪࡰࡪࠤࡩ࡯ࡲࡦࡥࡷࠤࡵࡿࡴࡦࡵࡷࠤ࡭ࡵ࡯࡬ࡵ࠱ࠎࠧࠨࠢॅ")
import pytest
import io
import os
from contextlib import redirect_stdout, redirect_stderr
import subprocess
import sys
def bstack11ll1l1l_opy_(bstack11l1lll1_opy_=None, bstack11l1llll_opy_=None):
    bstack11ll1ll_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡅࡲࡰࡱ࡫ࡣࡵࠢࡳࡽࡹ࡫ࡳࡵࠢࡷࡩࡸࡺࡳࠡࡷࡶ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠧࡴࠢ࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠤࡆࡖࡉࡴ࠰ࠍࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡵࡧࡶࡸࡤࡧࡲࡨࡵࠣࠬࡱ࡯ࡳࡵ࠮ࠣࡳࡵࡺࡩࡰࡰࡤࡰ࠮ࡀࠠࡄࡱࡰࡴࡱ࡫ࡴࡦࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡴࡾࡺࡥࡴࡶࠣࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠦࡩ࡯ࡥ࡯ࡹࡩ࡯࡮ࡨࠢࡳࡥࡹ࡮ࡳࠡࡣࡱࡨࠥ࡬࡬ࡢࡩࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡡ࡬ࡧࡶࠤࡵࡸࡥࡤࡧࡧࡩࡳࡩࡥࠡࡱࡹࡩࡷࠦࡴࡦࡵࡷࡣࡵࡧࡴࡩࡵࠣ࡭࡫ࠦࡢࡰࡶ࡫ࠤࡦࡸࡥࠡࡲࡵࡳࡻ࡯ࡤࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡺࡥࡴࡶࡢࡴࡦࡺࡨࡴࠢࠫࡰ࡮ࡹࡴࠡࡱࡵࠤࡸࡺࡲ࠭ࠢࡲࡴࡹ࡯࡯࡯ࡣ࡯࠭࠿ࠦࡔࡦࡵࡷࠤ࡫࡯࡬ࡦࠪࡶ࠭࠴ࡪࡩࡳࡧࡦࡸࡴࡸࡹࠩ࡫ࡨࡷ࠮ࠦࡴࡰࠢࡦࡳࡱࡲࡥࡤࡶࠣࡪࡷࡵ࡭࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡇࡦࡴࠠࡣࡧࠣࡥࠥࡹࡩ࡯ࡩ࡯ࡩࠥࡶࡡࡵࡪࠣࡷࡹࡸࡩ࡯ࡩࠣࡳࡷࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡱࡣࡷ࡬ࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡋࡪࡲࡴࡸࡥࡥࠢ࡬ࡪࠥࡺࡥࡴࡶࡢࡥࡷ࡭ࡳࠡ࡫ࡶࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩ࠴ࠊࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡥ࡫ࡦࡸ࠿ࠦࡃࡰ࡮࡯ࡩࡨࡺࡩࡰࡰࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡼ࡯ࡴࡩࠢ࡮ࡩࡾࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡵࡸࡧࡨ࡫ࡳࡴࠢࠫࡦࡴࡵ࡬ࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡦࡳࡺࡴࡴࠡࠪ࡬ࡲࡹ࠯ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠ࡯ࡱࡧࡩ࡮ࡪࡳࠡࠪ࡯࡭ࡸࡺࠩࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠥ࠮࡬ࡪࡵࡷ࠭ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥ࡫ࡲࡳࡱࡵࠤ࠭ࡹࡴࡳࠫࠍࠤࠥࠦࠠࠣࠤࠥॆ")
    try:
        bstack11l1ll11_opy_ = os.getenv(bstack11ll1ll_opy_ (u"ࠤࡓ࡝࡙ࡋࡓࡕࡡࡆ࡙ࡗࡘࡅࡏࡖࡢࡘࡊ࡙ࡔࠣे")) is not None
        if bstack11l1lll1_opy_ is not None:
            args = list(bstack11l1lll1_opy_)
        elif bstack11l1llll_opy_ is not None:
            if isinstance(bstack11l1llll_opy_, str):
                args = [bstack11l1llll_opy_]
            elif isinstance(bstack11l1llll_opy_, list):
                args = list(bstack11l1llll_opy_)
            else:
                args = [bstack11ll1ll_opy_ (u"ࠥ࠲ࠧै")]
        else:
            args = [bstack11ll1ll_opy_ (u"ࠦ࠳ࠨॉ")]
        if bstack11l1ll11_opy_:
            logger.debug(bstack11ll1ll_opy_ (u"ࠬࡡࡣࡰ࡮࡯ࡩࡨࡺ࡟ࡵࡧࡶࡸࡸࡥࡷࡪࡶ࡫ࡣࡵࡿࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࡠࠤࡈࡵ࡬࡭ࡧࡦࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࡹࠠࡷ࡫ࡤࠤࡸࡻࡢࡱࡴࡲࡧࡪࡹࡳࠨॊ"))
            return _11ll11l1_opy_(args)
        bstack11ll1111_opy_ = args + [
            bstack11ll1ll_opy_ (u"ࠨ࠭࠮ࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡲࡲࡱࡿࠢो"),
            bstack11ll1ll_opy_ (u"ࠢ࠮࠯ࡴࡹ࡮࡫ࡴࠣौ")
        ]
        class bstack11ll111l_opy_:
            bstack11ll1ll_opy_ (u"ࠣࠤࠥࡔࡾࡺࡥࡴࡶࠣࡴࡱࡻࡧࡪࡰࠣࡸ࡭ࡧࡴࠡࡥࡤࡴࡹࡻࡲࡦࡵࠣࡧࡴࡲ࡬ࡦࡥࡷࡩࡩࠦࡴࡦࡵࡷࠤ࡮ࡺࡥ࡮ࡵ࠱ࠦࠧࠨ्")
            def __init__(self):
                self.bstack11ll1ll1_opy_ = []
                self.test_files = set()
                self.bstack11ll11ll_opy_ = None
            def pytest_collection_finish(self, session):
                bstack11ll1ll_opy_ (u"ࠤࠥࠦࡍࡵ࡯࡬ࠢࡦࡥࡱࡲࡥࡥࠢࡤࡪࡹ࡫ࡲࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡯ࡳࠡࡨ࡬ࡲ࡮ࡹࡨࡦࡦ࠱ࠦࠧࠨॎ")
                try:
                    for item in session.items:
                        nodeid = item.nodeid
                        self.bstack11ll1ll1_opy_.append(nodeid)
                        if bstack11ll1ll_opy_ (u"ࠥ࠾࠿ࠨॏ") in nodeid:
                            file_path = nodeid.split(bstack11ll1ll_opy_ (u"ࠦ࠿ࡀࠢॐ"), 1)[0]
                            if file_path.endswith(bstack11ll1ll_opy_ (u"ࠬ࠴ࡰࡺࠩ॑")):
                                self.test_files.add(file_path)
                except Exception as e:
                    self.bstack11ll11ll_opy_ = str(e)
        collector = bstack11ll111l_opy_()
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            exit_code = pytest.main(bstack11ll1111_opy_, plugins=[collector])
        if collector.bstack11ll11ll_opy_:
            return {bstack11ll1ll_opy_ (u"ࠨࡳࡶࡥࡦࡩࡸࡹ॒ࠢ"): False, bstack11ll1ll_opy_ (u"ࠢࡤࡱࡸࡲࡹࠨ॓"): 0, bstack11ll1ll_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࡴࠤ॔"): [], bstack11ll1ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡸࠨॕ"): [], bstack11ll1ll_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤॖ"): bstack11ll1ll_opy_ (u"ࠦࡈࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠦॗ").format(collector.bstack11ll11ll_opy_)}
        return {
            bstack11ll1ll_opy_ (u"ࠧࡹࡵࡤࡥࡨࡷࡸࠨक़"): True,
            bstack11ll1ll_opy_ (u"ࠨࡣࡰࡷࡱࡸࠧख़"): len(collector.bstack11ll1ll1_opy_),
            bstack11ll1ll_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࡳࠣग़"): collector.bstack11ll1ll1_opy_,
            bstack11ll1ll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠧज़"): sorted(collector.test_files),
            bstack11ll1ll_opy_ (u"ࠤࡨࡼ࡮ࡺ࡟ࡤࡱࡧࡩࠧड़"): exit_code
        }
    except Exception as e:
        return {bstack11ll1ll_opy_ (u"ࠥࡷࡺࡩࡣࡦࡵࡶࠦढ़"): False, bstack11ll1ll_opy_ (u"ࠦࡨࡵࡵ࡯ࡶࠥफ़"): 0, bstack11ll1ll_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࡸࠨय़"): [], bstack11ll1ll_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯࡬ࡦࡵࠥॠ"): [], bstack11ll1ll_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨॡ"): bstack11ll1ll_opy_ (u"ࠣࡗࡱࡩࡽࡶࡥࡤࡶࡨࡨࠥ࡫ࡲࡳࡱࡵࠤ࡮ࡴࠠࡵࡧࡶࡸࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯࠼ࠣࡿࢂࠨॢ").format(e)}
def _11ll11l1_opy_(args):
    bstack11ll1ll_opy_ (u"ࠤࠥࠦࡎࡹ࡯࡭ࡣࡷࡩࡩࠦࡣࡰ࡮࡯ࡩࡨࡺࡩࡰࡰࠣࡩࡽ࡫ࡣࡶࡶࡨࡨࠥ࡯࡮ࠡࡣࠣࡷࡪࡶࡡࡳࡣࡷࡩࠥࡖࡹࡵࡪࡲࡲࠥࡶࡲࡰࡥࡨࡷࡸࠦࡴࡰࠢࡤࡺࡴ࡯ࡤࠡࡰࡨࡷࡹ࡫ࡤࠡࡲࡼࡸࡪࡹࡴࠡ࡫ࡶࡷࡺ࡫ࡳ࠯ࠤࠥࠦॣ")
    bstack11ll1lll_opy_ = [sys.executable, bstack11ll1ll_opy_ (u"ࠥ࠱ࡲࠨ।"), bstack11ll1ll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࠦ॥"), bstack11ll1ll_opy_ (u"ࠧ࠳࠭ࡤࡱ࡯ࡰࡪࡩࡴ࠮ࡱࡱࡰࡾࠨ०"), bstack11ll1ll_opy_ (u"ࠨ࠭࠮ࡳࡸ࡭ࡪࡺࠢ१")]
    bstack11ll1l11_opy_ = [a for a in args if a not in (bstack11ll1ll_opy_ (u"ࠢ࠮࠯ࡦࡳࡱࡲࡥࡤࡶ࠰ࡳࡳࡲࡹࠣ२"), bstack11ll1ll_opy_ (u"ࠣ࠯࠰ࡵࡺ࡯ࡥࡵࠤ३"), bstack11ll1ll_opy_ (u"ࠤ࠰ࡵࠧ४"))]
    cmd = bstack11ll1lll_opy_ + bstack11ll1l11_opy_
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, env=os.environ.copy())
        stdout = proc.stdout.splitlines()
        bstack11ll1ll1_opy_ = []
        test_files = set()
        for line in stdout:
            line = line.strip()
            if not line or bstack11ll1ll_opy_ (u"ࠥࠤࡨࡵ࡬࡭ࡧࡦࡸࡪࡪࠢ५") in line.lower():
                continue
            if bstack11ll1ll_opy_ (u"ࠦ࠿ࡀࠢ६") in line:
                bstack11ll1ll1_opy_.append(line)
                file_path = line.split(bstack11ll1ll_opy_ (u"ࠧࡀ࠺ࠣ७"), 1)[0]
                if file_path.endswith(bstack11ll1ll_opy_ (u"࠭࠮ࡱࡻࠪ८")):
                    test_files.add(file_path)
        success = proc.returncode in (0, 5)
        return {
            bstack11ll1ll_opy_ (u"ࠢࡴࡷࡦࡧࡪࡹࡳࠣ९"): success,
            bstack11ll1ll_opy_ (u"ࠣࡥࡲࡹࡳࡺࠢ॰"): len(bstack11ll1ll1_opy_),
            bstack11ll1ll_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࡵࠥॱ"): bstack11ll1ll1_opy_,
            bstack11ll1ll_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨ࡬ࡰࡪࡹࠢॲ"): sorted(test_files),
            bstack11ll1ll_opy_ (u"ࠦࡪࡾࡩࡵࡡࡦࡳࡩ࡫ࠢॳ"): proc.returncode,
            bstack11ll1ll_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦॴ"): None if success else bstack11ll1ll_opy_ (u"ࠨࡓࡶࡤࡳࡶࡴࡩࡥࡴࡵࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠠࠩࡧࡻ࡭ࡹࠦࡻࡾࠫࠥॵ").format(proc.returncode)
        }
    except Exception as e:
        return {bstack11ll1ll_opy_ (u"ࠢࡴࡷࡦࡧࡪࡹࡳࠣॶ"): False, bstack11ll1ll_opy_ (u"ࠣࡥࡲࡹࡳࡺࠢॷ"): 0, bstack11ll1ll_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࡵࠥॸ"): [], bstack11ll1ll_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨ࡬ࡰࡪࡹࠢॹ"): [], bstack11ll1ll_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥॺ"): bstack11ll1ll_opy_ (u"࡙ࠧࡵࡣࡲࡵࡳࡨ࡫ࡳࡴࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࠦࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠤॻ").format(e)}