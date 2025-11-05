# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
bstack11111_opy_ (u"ࠢࠣࠤࠍࡔࡾࡺࡥࡴࡶࠣࡸࡪࡹࡴࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡮ࡥ࡭ࡲࡨࡶࠥࡻࡳࡪࡰࡪࠤࡩ࡯ࡲࡦࡥࡷࠤࡵࡿࡴࡦࡵࡷࠤ࡭ࡵ࡯࡬ࡵ࠱ࠎࠧࠨࠢॅ")
import pytest
import io
import os
from contextlib import redirect_stdout, redirect_stderr
import subprocess
import sys
def bstack11ll1l1l_opy_(bstack11ll1l11_opy_=None, bstack11l1llll_opy_=None):
    bstack11111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡅࡲࡰࡱ࡫ࡣࡵࠢࡳࡽࡹ࡫ࡳࡵࠢࡷࡩࡸࡺࡳࠡࡷࡶ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠧࡴࠢ࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠤࡆࡖࡉࡴ࠰ࠍࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡵࡧࡶࡸࡤࡧࡲࡨࡵࠣࠬࡱ࡯ࡳࡵ࠮ࠣࡳࡵࡺࡩࡰࡰࡤࡰ࠮ࡀࠠࡄࡱࡰࡴࡱ࡫ࡴࡦࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡴࡾࡺࡥࡴࡶࠣࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠦࡩ࡯ࡥ࡯ࡹࡩ࡯࡮ࡨࠢࡳࡥࡹ࡮ࡳࠡࡣࡱࡨࠥ࡬࡬ࡢࡩࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡡ࡬ࡧࡶࠤࡵࡸࡥࡤࡧࡧࡩࡳࡩࡥࠡࡱࡹࡩࡷࠦࡴࡦࡵࡷࡣࡵࡧࡴࡩࡵࠣ࡭࡫ࠦࡢࡰࡶ࡫ࠤࡦࡸࡥࠡࡲࡵࡳࡻ࡯ࡤࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡺࡥࡴࡶࡢࡴࡦࡺࡨࡴࠢࠫࡰ࡮ࡹࡴࠡࡱࡵࠤࡸࡺࡲ࠭ࠢࡲࡴࡹ࡯࡯࡯ࡣ࡯࠭࠿ࠦࡔࡦࡵࡷࠤ࡫࡯࡬ࡦࠪࡶ࠭࠴ࡪࡩࡳࡧࡦࡸࡴࡸࡹࠩ࡫ࡨࡷ࠮ࠦࡴࡰࠢࡦࡳࡱࡲࡥࡤࡶࠣࡪࡷࡵ࡭࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡇࡦࡴࠠࡣࡧࠣࡥࠥࡹࡩ࡯ࡩ࡯ࡩࠥࡶࡡࡵࡪࠣࡷࡹࡸࡩ࡯ࡩࠣࡳࡷࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡱࡣࡷ࡬ࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡋࡪࡲࡴࡸࡥࡥࠢ࡬ࡪࠥࡺࡥࡴࡶࡢࡥࡷ࡭ࡳࠡ࡫ࡶࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩ࠴ࠊࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡥ࡫ࡦࡸ࠿ࠦࡃࡰ࡮࡯ࡩࡨࡺࡩࡰࡰࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡼ࡯ࡴࡩࠢ࡮ࡩࡾࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡵࡸࡧࡨ࡫ࡳࡴࠢࠫࡦࡴࡵ࡬ࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡦࡳࡺࡴࡴࠡࠪ࡬ࡲࡹ࠯ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠ࡯ࡱࡧࡩ࡮ࡪࡳࠡࠪ࡯࡭ࡸࡺࠩࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠥ࠮࡬ࡪࡵࡷ࠭ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥ࡫ࡲࡳࡱࡵࠤ࠭ࡹࡴࡳࠫࠍࠤࠥࠦࠠࠣࠤࠥॆ")
    try:
        bstack11ll11ll_opy_ = os.getenv(bstack11111_opy_ (u"ࠤࡓ࡝࡙ࡋࡓࡕࡡࡆ࡙ࡗࡘࡅࡏࡖࡢࡘࡊ࡙ࡔࠣे")) is not None
        if bstack11ll1l11_opy_ is not None:
            args = list(bstack11ll1l11_opy_)
        elif bstack11l1llll_opy_ is not None:
            if isinstance(bstack11l1llll_opy_, str):
                args = [bstack11l1llll_opy_]
            elif isinstance(bstack11l1llll_opy_, list):
                args = list(bstack11l1llll_opy_)
            else:
                args = [bstack11111_opy_ (u"ࠥ࠲ࠧै")]
        else:
            args = [bstack11111_opy_ (u"ࠦ࠳ࠨॉ")]
        if bstack11ll11ll_opy_:
            return _11ll111l_opy_(args)
        bstack11ll11l1_opy_ = args + [
            bstack11111_opy_ (u"ࠧ࠳࠭ࡤࡱ࡯ࡰࡪࡩࡴ࠮ࡱࡱࡰࡾࠨॊ"),
            bstack11111_opy_ (u"ࠨ࠭࠮ࡳࡸ࡭ࡪࡺࠢो")
        ]
        class bstack11ll1111_opy_:
            bstack11111_opy_ (u"ࠢࠣࠤࡓࡽࡹ࡫ࡳࡵࠢࡳࡰࡺ࡭ࡩ࡯ࠢࡷ࡬ࡦࡺࠠࡤࡣࡳࡸࡺࡸࡥࡴࠢࡦࡳࡱࡲࡥࡤࡶࡨࡨࠥࡺࡥࡴࡶࠣ࡭ࡹ࡫࡭ࡴ࠰ࠥࠦࠧौ")
            def __init__(self):
                self.bstack11l1lll1_opy_ = []
                self.test_files = set()
                self.bstack11l1ll11_opy_ = None
            def pytest_collection_finish(self, session):
                bstack11111_opy_ (u"ࠣࠤࠥࡌࡴࡵ࡫ࠡࡥࡤࡰࡱ࡫ࡤࠡࡣࡩࡸࡪࡸࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡱࡱࠤ࡮ࡹࠠࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥ࠰्ࠥࠦࠧ")
                try:
                    for item in session.items:
                        nodeid = item.nodeid
                        self.bstack11l1lll1_opy_.append(nodeid)
                        if bstack11111_opy_ (u"ࠤ࠽࠾ࠧॎ") in nodeid:
                            file_path = nodeid.split(bstack11111_opy_ (u"ࠥ࠾࠿ࠨॏ"), 1)[0]
                            if file_path.endswith(bstack11111_opy_ (u"ࠫ࠳ࡶࡹࠨॐ")):
                                self.test_files.add(file_path)
                except Exception as e:
                    self.bstack11l1ll11_opy_ = str(e)
        collector = bstack11ll1111_opy_()
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            exit_code = pytest.main(bstack11ll11l1_opy_, plugins=[collector])
        if collector.bstack11l1ll11_opy_:
            return {bstack11111_opy_ (u"ࠧࡹࡵࡤࡥࡨࡷࡸࠨ॑"): False, bstack11111_opy_ (u"ࠨࡣࡰࡷࡱࡸ॒ࠧ"): 0, bstack11111_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࡳࠣ॓"): [], bstack11111_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠧ॔"): [], bstack11111_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣॕ"): bstack11111_opy_ (u"ࠥࡇࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴࠠࡦࡴࡵࡳࡷࡀࠠࡼࡿࠥॖ").format(collector.bstack11l1ll11_opy_)}
        return {
            bstack11111_opy_ (u"ࠦࡸࡻࡣࡤࡧࡶࡷࠧॗ"): True,
            bstack11111_opy_ (u"ࠧࡩ࡯ࡶࡰࡷࠦक़"): len(collector.bstack11l1lll1_opy_),
            bstack11111_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࡹࠢख़"): collector.bstack11l1lll1_opy_,
            bstack11111_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡶࠦग़"): sorted(collector.test_files),
            bstack11111_opy_ (u"ࠣࡧࡻ࡭ࡹࡥࡣࡰࡦࡨࠦज़"): exit_code
        }
    except Exception as e:
        return {bstack11111_opy_ (u"ࠤࡶࡹࡨࡩࡥࡴࡵࠥड़"): False, bstack11111_opy_ (u"ࠥࡧࡴࡻ࡮ࡵࠤढ़"): 0, bstack11111_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࡷࠧफ़"): [], bstack11111_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪ࡮ࡲࡥࡴࠤय़"): [], bstack11111_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧॠ"): bstack11111_opy_ (u"ࠢࡖࡰࡨࡼࡵ࡫ࡣࡵࡧࡧࠤࡪࡸࡲࡰࡴࠣ࡭ࡳࠦࡴࡦࡵࡷࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠧॡ").format(e)}
def _11ll111l_opy_(args):
    bstack11111_opy_ (u"ࠣࠤࠥࡍࡸࡵ࡬ࡢࡶࡨࡨࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯ࠢࡨࡼࡪࡩࡵࡵࡧࡧࠤ࡮ࡴࠠࡢࠢࡶࡩࡵࡧࡲࡢࡶࡨࠤࡕࡿࡴࡩࡱࡱࠤࡵࡸ࡯ࡤࡧࡶࡷࠥࡺ࡯ࠡࡣࡹࡳ࡮ࡪࠠ࡯ࡧࡶࡸࡪࡪࠠࡱࡻࡷࡩࡸࡺࠠࡪࡵࡶࡹࡪࡹ࠮ࠣࠤࠥॢ")
    bstack11ll1ll1_opy_ = [sys.executable, bstack11111_opy_ (u"ࠤ࠰ࡱࠧॣ"), bstack11111_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶࠥ।"), bstack11111_opy_ (u"ࠦ࠲࠳ࡣࡰ࡮࡯ࡩࡨࡺ࠭ࡰࡰ࡯ࡽࠧ॥"), bstack11111_opy_ (u"ࠧ࠳࠭ࡲࡷ࡬ࡩࡹࠨ०")]
    bstack11ll1lll_opy_ = [a for a in args if a not in (bstack11111_opy_ (u"ࠨ࠭࠮ࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡲࡲࡱࡿࠢ१"), bstack11111_opy_ (u"ࠢ࠮࠯ࡴࡹ࡮࡫ࡴࠣ२"), bstack11111_opy_ (u"ࠣ࠯ࡴࠦ३"))]
    cmd = bstack11ll1ll1_opy_ + bstack11ll1lll_opy_
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, env=os.environ.copy())
        stdout = proc.stdout.splitlines()
        bstack11l1lll1_opy_ = []
        test_files = set()
        for line in stdout:
            line = line.strip()
            if not line or bstack11111_opy_ (u"ࠤࠣࡧࡴࡲ࡬ࡦࡥࡷࡩࡩࠨ४") in line.lower():
                continue
            if bstack11111_opy_ (u"ࠥ࠾࠿ࠨ५") in line:
                bstack11l1lll1_opy_.append(line)
                file_path = line.split(bstack11111_opy_ (u"ࠦ࠿ࡀࠢ६"), 1)[0]
                if file_path.endswith(bstack11111_opy_ (u"ࠬ࠴ࡰࡺࠩ७")):
                    test_files.add(file_path)
        success = proc.returncode in (0, 5)
        return {
            bstack11111_opy_ (u"ࠨࡳࡶࡥࡦࡩࡸࡹࠢ८"): success,
            bstack11111_opy_ (u"ࠢࡤࡱࡸࡲࡹࠨ९"): len(bstack11l1lll1_opy_),
            bstack11111_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࡴࠤ॰"): bstack11l1lll1_opy_,
            bstack11111_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡸࠨॱ"): sorted(test_files),
            bstack11111_opy_ (u"ࠥࡩࡽ࡯ࡴࡠࡥࡲࡨࡪࠨॲ"): proc.returncode,
            bstack11111_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥॳ"): None if success else bstack11111_opy_ (u"࡙ࠧࡵࡣࡲࡵࡳࡨ࡫ࡳࡴࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࠦࠨࡦࡺ࡬ࡸࠥࢁࡽࠪࠤॴ").format(proc.returncode)
        }
    except Exception as e:
        return {bstack11111_opy_ (u"ࠨࡳࡶࡥࡦࡩࡸࡹࠢॵ"): False, bstack11111_opy_ (u"ࠢࡤࡱࡸࡲࡹࠨॶ"): 0, bstack11111_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࡴࠤॷ"): [], bstack11111_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡸࠨॸ"): [], bstack11111_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤॹ"): bstack11111_opy_ (u"ࠦࡘࡻࡢࡱࡴࡲࡧࡪࡹࡳࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠣॺ").format(e)}