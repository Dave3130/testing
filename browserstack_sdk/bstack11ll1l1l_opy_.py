# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
bstack11l11ll_opy_ (u"ࠢࠣࠤࠍࡔࡾࡺࡥࡴࡶࠣࡸࡪࡹࡴࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡮ࡥ࡭ࡲࡨࡶࠥࡻࡳࡪࡰࡪࠤࡩ࡯ࡲࡦࡥࡷࠤࡵࡿࡴࡦࡵࡷࠤ࡭ࡵ࡯࡬ࡵ࠱ࠎࠧࠨࠢॅ")
import pytest
import io
import os
from contextlib import redirect_stdout, redirect_stderr
import subprocess
import sys
def bstack11ll11ll_opy_(bstack11ll11l1_opy_=None, bstack11ll1111_opy_=None):
    bstack11l11ll_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡅࡲࡰࡱ࡫ࡣࡵࠢࡳࡽࡹ࡫ࡳࡵࠢࡷࡩࡸࡺࡳࠡࡷࡶ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠧࡴࠢ࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠤࡆࡖࡉࡴ࠰ࠍࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡵࡧࡶࡸࡤࡧࡲࡨࡵࠣࠬࡱ࡯ࡳࡵ࠮ࠣࡳࡵࡺࡩࡰࡰࡤࡰ࠮ࡀࠠࡄࡱࡰࡴࡱ࡫ࡴࡦࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡴࡾࡺࡥࡴࡶࠣࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠦࡩ࡯ࡥ࡯ࡹࡩ࡯࡮ࡨࠢࡳࡥࡹ࡮ࡳࠡࡣࡱࡨࠥ࡬࡬ࡢࡩࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡡ࡬ࡧࡶࠤࡵࡸࡥࡤࡧࡧࡩࡳࡩࡥࠡࡱࡹࡩࡷࠦࡴࡦࡵࡷࡣࡵࡧࡴࡩࡵࠣ࡭࡫ࠦࡢࡰࡶ࡫ࠤࡦࡸࡥࠡࡲࡵࡳࡻ࡯ࡤࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡺࡥࡴࡶࡢࡴࡦࡺࡨࡴࠢࠫࡰ࡮ࡹࡴࠡࡱࡵࠤࡸࡺࡲ࠭ࠢࡲࡴࡹ࡯࡯࡯ࡣ࡯࠭࠿ࠦࡔࡦࡵࡷࠤ࡫࡯࡬ࡦࠪࡶ࠭࠴ࡪࡩࡳࡧࡦࡸࡴࡸࡹࠩ࡫ࡨࡷ࠮ࠦࡴࡰࠢࡦࡳࡱࡲࡥࡤࡶࠣࡪࡷࡵ࡭࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡇࡦࡴࠠࡣࡧࠣࡥࠥࡹࡩ࡯ࡩ࡯ࡩࠥࡶࡡࡵࡪࠣࡷࡹࡸࡩ࡯ࡩࠣࡳࡷࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡱࡣࡷ࡬ࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡋࡪࡲࡴࡸࡥࡥࠢ࡬ࡪࠥࡺࡥࡴࡶࡢࡥࡷ࡭ࡳࠡ࡫ࡶࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩ࠴ࠊࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡥ࡫ࡦࡸ࠿ࠦࡃࡰ࡮࡯ࡩࡨࡺࡩࡰࡰࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡼ࡯ࡴࡩࠢ࡮ࡩࡾࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡵࡸࡧࡨ࡫ࡳࡴࠢࠫࡦࡴࡵ࡬ࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡦࡳࡺࡴࡴࠡࠪ࡬ࡲࡹ࠯ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠ࡯ࡱࡧࡩ࡮ࡪࡳࠡࠪ࡯࡭ࡸࡺࠩࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠥ࠮࡬ࡪࡵࡷ࠭ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥ࡫ࡲࡳࡱࡵࠤ࠭ࡹࡴࡳࠫࠍࠤࠥࠦࠠࠣࠤࠥॆ")
    try:
        bstack11l1llll_opy_ = os.getenv(bstack11l11ll_opy_ (u"ࠤࡓ࡝࡙ࡋࡓࡕࡡࡆ࡙ࡗࡘࡅࡏࡖࡢࡘࡊ࡙ࡔࠣे")) is not None
        if bstack11ll11l1_opy_ is not None:
            args = list(bstack11ll11l1_opy_)
        elif bstack11ll1111_opy_ is not None:
            if isinstance(bstack11ll1111_opy_, str):
                args = [bstack11ll1111_opy_]
            elif isinstance(bstack11ll1111_opy_, list):
                args = list(bstack11ll1111_opy_)
            else:
                args = [bstack11l11ll_opy_ (u"ࠥ࠲ࠧै")]
        else:
            args = [bstack11l11ll_opy_ (u"ࠦ࠳ࠨॉ")]
        if bstack11l1llll_opy_:
            return _11l1ll11_opy_(args)
        bstack11ll1lll_opy_ = args + [
            bstack11l11ll_opy_ (u"ࠧ࠳࠭ࡤࡱ࡯ࡰࡪࡩࡴ࠮ࡱࡱࡰࡾࠨॊ"),
            bstack11l11ll_opy_ (u"ࠨ࠭࠮ࡳࡸ࡭ࡪࡺࠢो")
        ]
        class bstack11l1ll1l_opy_:
            bstack11l11ll_opy_ (u"ࠢࠣࠤࡓࡽࡹ࡫ࡳࡵࠢࡳࡰࡺ࡭ࡩ࡯ࠢࡷ࡬ࡦࡺࠠࡤࡣࡳࡸࡺࡸࡥࡴࠢࡦࡳࡱࡲࡥࡤࡶࡨࡨࠥࡺࡥࡴࡶࠣ࡭ࡹ࡫࡭ࡴ࠰ࠥࠦࠧौ")
            def __init__(self):
                self.bstack11l1lll1_opy_ = []
                self.test_files = set()
                self.bstack11l1l1ll_opy_ = None
            def pytest_collection_finish(self, session):
                bstack11l11ll_opy_ (u"ࠣࠤࠥࡌࡴࡵ࡫ࠡࡥࡤࡰࡱ࡫ࡤࠡࡣࡩࡸࡪࡸࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡱࡱࠤ࡮ࡹࠠࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥ࠰्ࠥࠦࠧ")
                try:
                    for item in session.items:
                        nodeid = item.nodeid
                        self.bstack11l1lll1_opy_.append(nodeid)
                        if bstack11l11ll_opy_ (u"ࠤ࠽࠾ࠧॎ") in nodeid:
                            file_path = nodeid.split(bstack11l11ll_opy_ (u"ࠥ࠾࠿ࠨॏ"), 1)[0]
                            if file_path.endswith(bstack11l11ll_opy_ (u"ࠫ࠳ࡶࡹࠨॐ")):
                                self.test_files.add(file_path)
                except Exception as e:
                    self.bstack11l1l1ll_opy_ = str(e)
        collector = bstack11l1ll1l_opy_()
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            exit_code = pytest.main(bstack11ll1lll_opy_, plugins=[collector])
        if collector.bstack11l1l1ll_opy_:
            return {bstack11l11ll_opy_ (u"ࠧࡹࡵࡤࡥࡨࡷࡸࠨ॑"): False, bstack11l11ll_opy_ (u"ࠨࡣࡰࡷࡱࡸ॒ࠧ"): 0, bstack11l11ll_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࡳࠣ॓"): [], bstack11l11ll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠧ॔"): [], bstack11l11ll_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣॕ"): bstack11ll111l_opy_ (u"ࠥࡇࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴࠠࡦࡴࡵࡳࡷࡀࠠࡼࡥࡲࡰࡱ࡫ࡣࡵࡱࡵ࠲ࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮ࡠࡧࡵࡶࡴࡸࡽࠣॖ")}
        return {
            bstack11l11ll_opy_ (u"ࠦࡸࡻࡣࡤࡧࡶࡷࠧॗ"): True,
            bstack11l11ll_opy_ (u"ࠧࡩ࡯ࡶࡰࡷࠦक़"): len(collector.bstack11l1lll1_opy_),
            bstack11l11ll_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࡹࠢख़"): collector.bstack11l1lll1_opy_,
            bstack11l11ll_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡶࠦग़"): sorted(collector.test_files),
            bstack11l11ll_opy_ (u"ࠣࡧࡻ࡭ࡹࡥࡣࡰࡦࡨࠦज़"): exit_code
        }
    except Exception as e:
        return {bstack11l11ll_opy_ (u"ࠤࡶࡹࡨࡩࡥࡴࡵࠥड़"): False, bstack11l11ll_opy_ (u"ࠥࡧࡴࡻ࡮ࡵࠤढ़"): 0, bstack11l11ll_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࡷࠧफ़"): [], bstack11l11ll_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪ࡮ࡲࡥࡴࠤय़"): [], bstack11l11ll_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧॠ"): bstack11ll111l_opy_ (u"ࠢࡖࡰࡨࡼࡵ࡫ࡣࡵࡧࡧࠤࡪࡸࡲࡰࡴࠣ࡭ࡳࠦࡴࡦࡵࡷࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮࠻ࠢࡾࡩࢂࠨॡ")}
def _11l1ll11_opy_(args):
    bstack11l11ll_opy_ (u"ࠣࠤࠥࡍࡸࡵ࡬ࡢࡶࡨࡨࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯ࠢࡨࡼࡪࡩࡵࡵࡧࡧࠤ࡮ࡴࠠࡢࠢࡶࡩࡵࡧࡲࡢࡶࡨࠤࡕࡿࡴࡩࡱࡱࠤࡵࡸ࡯ࡤࡧࡶࡷࠥࡺ࡯ࠡࡣࡹࡳ࡮ࡪࠠ࡯ࡧࡶࡸࡪࡪࠠࡱࡻࡷࡩࡸࡺࠠࡪࡵࡶࡹࡪࡹ࠮ࠣࠤࠥॢ")
    bstack11ll1l11_opy_ = [sys.executable, bstack11l11ll_opy_ (u"ࠤ࠰ࡱࠧॣ"), bstack11l11ll_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶࠥ।"), bstack11l11ll_opy_ (u"ࠦ࠲࠳ࡣࡰ࡮࡯ࡩࡨࡺ࠭ࡰࡰ࡯ࡽࠧ॥"), bstack11l11ll_opy_ (u"ࠧ࠳࠭ࡲࡷ࡬ࡩࡹࠨ०")]
    bstack11ll1ll1_opy_ = [a for a in args if a not in (bstack11l11ll_opy_ (u"ࠨ࠭࠮ࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡲࡲࡱࡿࠢ१"), bstack11l11ll_opy_ (u"ࠢ࠮࠯ࡴࡹ࡮࡫ࡴࠣ२"), bstack11l11ll_opy_ (u"ࠣ࠯ࡴࠦ३"))]
    cmd = bstack11ll1l11_opy_ + bstack11ll1ll1_opy_
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, env=os.environ.copy())
        stdout = proc.stdout.splitlines()
        bstack11l1lll1_opy_ = []
        test_files = set()
        for line in stdout:
            line = line.strip()
            if not line or bstack11l11ll_opy_ (u"ࠤࠣࡧࡴࡲ࡬ࡦࡥࡷࡩࡩࠨ४") in line.lower():
                continue
            if bstack11l11ll_opy_ (u"ࠥ࠾࠿ࠨ५") in line:
                bstack11l1lll1_opy_.append(line)
                file_path = line.split(bstack11l11ll_opy_ (u"ࠦ࠿ࡀࠢ६"), 1)[0]
                if file_path.endswith(bstack11l11ll_opy_ (u"ࠬ࠴ࡰࡺࠩ७")):
                    test_files.add(file_path)
        success = proc.returncode in (0, 5)
        return {
            bstack11l11ll_opy_ (u"ࠨࡳࡶࡥࡦࡩࡸࡹࠢ८"): success,
            bstack11l11ll_opy_ (u"ࠢࡤࡱࡸࡲࡹࠨ९"): len(bstack11l1lll1_opy_),
            bstack11l11ll_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࡴࠤ॰"): bstack11l1lll1_opy_,
            bstack11l11ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡸࠨॱ"): sorted(test_files),
            bstack11l11ll_opy_ (u"ࠥࡩࡽ࡯ࡴࡠࡥࡲࡨࡪࠨॲ"): proc.returncode,
            bstack11l11ll_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥॳ"): None if success else bstack11ll111l_opy_ (u"࡙ࠧࡵࡣࡲࡵࡳࡨ࡫ࡳࡴࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࠦࠨࡦࡺ࡬ࡸࠥࢁࡰࡳࡱࡦ࠲ࡷ࡫ࡴࡶࡴࡱࡧࡴࡪࡥࡾࠫࠥॴ")
        }
    except Exception as e:
        return {bstack11l11ll_opy_ (u"ࠨࡳࡶࡥࡦࡩࡸࡹࠢॵ"): False, bstack11l11ll_opy_ (u"ࠢࡤࡱࡸࡲࡹࠨॶ"): 0, bstack11l11ll_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࡴࠤॷ"): [], bstack11l11ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡸࠨॸ"): [], bstack11l11ll_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤॹ"): bstack11ll111l_opy_ (u"ࠦࡘࡻࡢࡱࡴࡲࡧࡪࡹࡳࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡥࡾࠤॺ")}