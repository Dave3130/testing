# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack1lllllll1_opy_
import subprocess
import re
from browserstack_sdk.bstack111111l1_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l111ll_opy_
from bstack_utils.bstack1111llll_opy_ import bstack11111l1l_opy_
from bstack_utils.constants import bstack11111l11_opy_
from bstack_utils.bstack1111lll1_opy_ import bstack111lll11_opy_
class bstack111l1l11_opy_:
    bstack1lll1lll1_opy_ = bstack1ll1l_opy_ (u"ࡲࠨ࠾ࡐࡳࡩࡻ࡬ࡦࠢࠫ࡟ࡣࡄ࡝ࠬࠫࡁࠫ঒")  # bstack11l1111l_opy_ lines bstack11_opy_ <Module path/to/bstack1111l111_opy_.py> in pytest --collect-bstack11l111l1_opy_ output
    def __init__(self, args, logger, bstack111l1111_opy_, bstack111ll1ll_opy_):
        self.args = args
        self.logger = logger
        self.bstack111l1111_opy_ = bstack111l1111_opy_
        self.bstack111ll1ll_opy_ = bstack111ll1ll_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1lllll11l_opy_ = []
        self.bstack1111ll11_opy_ = []
        self.bstack111llll1_opy_ = []
        self.bstack1llll1111_opy_ = self.bstack111l11ll_opy_()
        self.bstack1111l1l1_opy_ = -1
    def bstack1111111l_opy_(self, bstack11111lll_opy_):
        self.parse_args()
        self.bstack111l111l_opy_()
        self.bstack11l11lll_opy_(bstack11111lll_opy_)
        self.bstack1llllllll_opy_()
    def bstack11l11ll1_opy_(self):
        bstack1111lll1_opy_ = bstack111lll11_opy_.bstack111l1ll1_opy_(self.bstack111l1111_opy_, self.logger)
        if bstack1111lll1_opy_ is None:
            self.logger.warn(bstack1ll1l_opy_ (u"ࠣࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡪࡤࡲࡩࡲࡥࡳࠢ࡬ࡷࠥࡴ࡯ࡵࠢ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪࡪ࠮ࠡࡕ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦও"))
            return
        bstack111lllll_opy_ = False
        bstack1111lll1_opy_.bstack111ll11l_opy_(bstack1ll1l_opy_ (u"ࠤࡨࡲࡦࡨ࡬ࡦࡦࠥঔ"), bstack1111lll1_opy_.bstack11111ll1_opy_())
        start_time = time.time()
        if bstack1111lll1_opy_.bstack11111ll1_opy_():
            test_files = self.bstack111l1l1l_opy_()
            bstack111lllll_opy_ = True
            bstack1lll1llll_opy_ = bstack1111lll1_opy_.bstack1llllll1l_opy_(test_files)
            if bstack1lll1llll_opy_:
                self.bstack1lllll11l_opy_ = [os.path.normpath(item).replace(bstack1ll1l_opy_ (u"ࠪࡠࡡ࠭ক"), bstack1ll1l_opy_ (u"ࠫ࠴࠭খ")) for item in bstack1lll1llll_opy_]
                self.__1lll1ll11_opy_()
                bstack1111lll1_opy_.bstack111l1lll_opy_(bstack111lllll_opy_)
                self.logger.info(bstack1ll1l_opy_ (u"࡚ࠧࡥࡴࡶࡶࠤࡷ࡫࡯ࡳࡦࡨࡶࡪࡪࠠࡶࡵ࡬ࡲ࡬ࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡀࠠࡼࡿࠥগ").format(self.bstack1lllll11l_opy_))
            else:
                self.logger.info(bstack1ll1l_opy_ (u"ࠨࡎࡰࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡷࡦࡴࡨࠤࡷ࡫࡯ࡳࡦࡨࡶࡪࡪࠠࡣࡻࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦঘ"))
        bstack1111lll1_opy_.bstack111ll11l_opy_(bstack1ll1l_opy_ (u"ࠢࡵ࡫ࡰࡩ࡙ࡧ࡫ࡦࡰࡗࡳࡆࡶࡰ࡭ࡻࠥঙ"), int((time.time() - start_time) * 1000)) # bstack1llll1ll1_opy_ to bstack1lllll1ll_opy_
    def __1lll1ll11_opy_(self):
        bstack1ll1l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡌ࡯ࡳࠢࡨࡥࡨ࡮ࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࠣ࡭ࡳࠦࡳࡦ࡮ࡩ࠲ࡸࡶࡥࡤࡡࡩ࡭ࡱ࡫ࡳ࠭ࠢࡦࡳࡱࡲࡥࡤࡶࠣࡥࡱࡲࠠ࡯ࡱࡧࡩ࡮ࡪࡳࠡࡷࡶ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠠ࠮࠯ࡦࡳࡱࡲࡥࡤࡶ࠰ࡳࡳࡲࡹࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧচ")
        bstack1llll11ll_opy_ = []
        for bstack1111l111_opy_ in self.bstack1lllll11l_opy_:
            bstack1llllll11_opy_ = [bstack1ll1l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵࠤছ"), bstack1111l111_opy_, bstack1ll1l_opy_ (u"ࠥ࠱࠲ࡩ࡯࡭࡮ࡨࡧࡹ࠳࡯࡯࡮ࡼࠦজ"), bstack1ll1l_opy_ (u"ࠦ࠲ࡷࠢঝ")]
            result = subprocess.run(bstack1llllll11_opy_, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.stderr:
                self.logger.info(bstack1ll1l_opy_ (u"ࠧ࡝ࡡࡳࡰ࡬ࡲ࡬ࡹࠠࡥࡷࡵ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯࠼ࠣࡿࢂࠨঞ").format(result.stderr))
            if result.returncode != 0 and not result.stdout:
                self.logger.error(bstack1ll1l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࡹ࠺ࠡࡽࢀࠦট").format(result.stderr))
                continue
            self.logger.info(bstack1ll1l_opy_ (u"ࠢࡄࡱ࡯ࡰࡪࡩࡴࡪࡰࡪࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡦࡦࠣࡷࡪࡲࡥࡤࡶࡲࡶ࠿ࠦࡻࡾࠤঠ").format(result.stdout))
            for line in result.stdout.splitlines():
                line = line.strip()
                if line and not line.startswith(bstack1ll1l_opy_ (u"ࠣ࠾ࠥড")) and bstack1ll1l_opy_ (u"ࠤ࠽࠾ࠧঢ") in line:
                    bstack1llll11ll_opy_.append(line)
        os.environ[bstack1ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡒࡖࡈࡎࡅࡔࡖࡕࡅ࡙ࡋࡄࡠࡕࡈࡐࡊࡉࡔࡐࡔࡖࠫণ")] = json.dumps(bstack1llll11ll_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack11l1l111_opy_():
        import importlib
        if getattr(importlib, bstack1ll1l_opy_ (u"ࠫ࡫࡯࡮ࡥࡡ࡯ࡳࡦࡪࡥࡳࠩত"), False):
            bstack1llll11l1_opy_ = importlib.find_loader(bstack1ll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧথ"))
        else:
            bstack1llll11l1_opy_ = importlib.util.find_spec(bstack1ll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨদ"))
    def bstack1llll1l11_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1111l1l1_opy_ = -1
        if self.bstack111ll1ll_opy_ and bstack1ll1l_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧধ") in self.bstack111l1111_opy_:
            self.bstack1111l1l1_opy_ = int(self.bstack111l1111_opy_[bstack1ll1l_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨন")])
        try:
            bstack11l11111_opy_ = [bstack1ll1l_opy_ (u"ࠩ࠰࠱ࡩࡸࡩࡷࡧࡵࠫ঩"), bstack1ll1l_opy_ (u"ࠪ࠱࠲ࡶ࡬ࡶࡩ࡬ࡲࡸ࠭প"), bstack1ll1l_opy_ (u"ࠫ࠲ࡶࠧফ")]
            if self.bstack1111l1l1_opy_ >= 0:
                bstack11l11111_opy_.extend([bstack1ll1l_opy_ (u"ࠬ࠳࠭࡯ࡷࡰࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭ব"), bstack1ll1l_opy_ (u"࠭࠭࡯ࠩভ")])
            for arg in bstack11l11111_opy_:
                self.bstack1llll1l11_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack111l111l_opy_(self):
        bstack1111ll11_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack1111ll11_opy_ = bstack1111ll11_opy_
        return self.bstack1111ll11_opy_
    def bstack111ll111_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack11l1l111_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack11l111ll_opy_)
    def bstack11l11lll_opy_(self, bstack11111lll_opy_):
        bstack111111ll_opy_ = Config.bstack111l1ll1_opy_()
        if bstack11111lll_opy_:
            self.bstack1111ll11_opy_.append(bstack1ll1l_opy_ (u"ࠧ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫম"))
            self.bstack1111ll11_opy_.append(bstack1ll1l_opy_ (u"ࠨࡖࡵࡹࡪ࠭য"))
        if bstack111111ll_opy_.bstack1lll1l1ll_opy_():
            self.bstack1111ll11_opy_.append(bstack1ll1l_opy_ (u"ࠩ࠰࠱ࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨর"))
            self.bstack1111ll11_opy_.append(bstack1ll1l_opy_ (u"ࠪࡘࡷࡻࡥࠨ঱"))
        self.bstack1111ll11_opy_.append(bstack1ll1l_opy_ (u"ࠫ࠲ࡶࠧল"))
        self.bstack1111ll11_opy_.append(bstack1ll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡴࡱࡻࡧࡪࡰࠪ঳"))
        self.bstack1111ll11_opy_.append(bstack1ll1l_opy_ (u"࠭࠭࠮ࡦࡵ࡭ࡻ࡫ࡲࠨ঴"))
        self.bstack1111ll11_opy_.append(bstack1ll1l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ঵"))
        if self.bstack1111l1l1_opy_ > 1:
            self.bstack1111ll11_opy_.append(bstack1ll1l_opy_ (u"ࠨ࠯ࡱࠫশ"))
            self.bstack1111ll11_opy_.append(str(self.bstack1111l1l1_opy_))
    def bstack1llllllll_opy_(self):
        if bstack11111l1l_opy_.bstack1111ll1l_opy_(self.bstack111l1111_opy_):
             self.bstack1111ll11_opy_ += [
                bstack11111l11_opy_.get(bstack1ll1l_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࠨষ")), str(bstack11111l1l_opy_.bstack11l11l11_opy_(self.bstack111l1111_opy_)),
                bstack11111l11_opy_.get(bstack1ll1l_opy_ (u"ࠪࡨࡪࡲࡡࡺࠩস")), str(bstack11111l11_opy_.get(bstack1ll1l_opy_ (u"ࠫࡷ࡫ࡲࡶࡰ࠰ࡨࡪࡲࡡࡺࠩহ")))
            ]
    def bstack11l11l1l_opy_(self):
        bstack111llll1_opy_ = []
        for spec in self.bstack1lllll11l_opy_:
            bstack11111111_opy_ = [spec]
            bstack11111111_opy_ += self.bstack1111ll11_opy_
            bstack111llll1_opy_.append(bstack11111111_opy_)
        self.bstack111llll1_opy_ = bstack111llll1_opy_
        return bstack111llll1_opy_
    def bstack111l11ll_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack1llll1111_opy_ = True
            return True
        except Exception as e:
            self.bstack1llll1111_opy_ = False
        return self.bstack1llll1111_opy_
    def bstack1lll1ll1l_opy_(self):
        bstack1ll1l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡇࡦࡶࠣࡸ࡭࡫ࠠࡤࡱࡸࡲࡹࠦ࡯ࡧࠢࡷࡩࡸࡺࡳࠡࡹ࡬ࡸ࡭ࡵࡵࡵࠢࡵࡹࡳࡴࡩ࡯ࡩࠣࡸ࡭࡫࡭ࠡࡷࡶ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠧࡴࠢ࠰࠱ࡨࡵ࡬࡭ࡧࡦࡸ࠲ࡵ࡮࡭ࡻࠣࡪࡱࡧࡧ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡮ࡴࡴ࠻ࠢࡗ࡬ࡪࠦࡴࡰࡶࡤࡰࠥࡴࡵ࡮ࡤࡨࡶࠥࡵࡦࠡࡶࡨࡷࡹࡹࠠࡤࡱ࡯ࡰࡪࡩࡴࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣ঺")
        try:
            self.logger.info(bstack1ll1l_opy_ (u"ࠨࡃࡰ࡮࡯ࡩࡨࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࡴࠢࡸࡷ࡮ࡴࡧࠡࡲࡼࡸࡪࡹࡴࠡ࠯࠰ࡧࡴࡲ࡬ࡦࡥࡷ࠱ࡴࡴ࡬ࡺࠤ঻"))
            bstack1llllll11_opy_ = [bstack1ll1l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ়ࠢ"), *self.bstack1111ll11_opy_, bstack1ll1l_opy_ (u"ࠣ࠯࠰ࡧࡴࡲ࡬ࡦࡥࡷ࠱ࡴࡴ࡬ࡺࠤঽ")]
            result = subprocess.run(bstack1llllll11_opy_, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.stderr:
                self.logger.info(bstack1ll1l_opy_ (u"ࠤ࡚ࡥࡷࡴࡩ࡯ࡩࡶࠤࡩࡻࡲࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡦࡳࡺࡴࡴࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤা").format(result.stderr))
            if result.returncode != 0 and not result.stdout:
                self.logger.error(bstack1ll1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࡶࠤࡨࡵࡵ࡯ࡶ࠽ࠤࢀࢃࠢি").format(result.stderr))
                return 0
            test_count = result.stdout.count(bstack1ll1l_opy_ (u"ࠦࡁࡌࡵ࡯ࡥࡷ࡭ࡴࡴࠠࠣী"))
            self.logger.info(bstack1ll1l_opy_ (u"࡚ࠧ࡯ࡵࡣ࡯ࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡲ࡬ࡦࡥࡷࡩࡩࡀࠠࡼࡿࠥু").format(test_count))
            return test_count
        except Exception as e:
            self.logger.error(bstack1ll1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡤࡱࡸࡲࡹࡀࠠࡼࡿࠥূ").format(e))
            return 0
    def bstack1llll1lll_opy_(self, bstack1111l11l_opy_, bstack1111111l_opy_):
        bstack1111111l_opy_[bstack1ll1l_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧৃ")] = self.bstack111l1111_opy_
        multiprocessing.set_start_method(bstack1ll1l_opy_ (u"ࠨࡵࡳࡥࡼࡴࠧৄ"))
        bstack1llll1l1l_opy_ = []
        manager = multiprocessing.Manager()
        bstack11l1l11l_opy_ = manager.list()
        if bstack1ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ৅") in self.bstack111l1111_opy_:
            for index, platform in enumerate(self.bstack111l1111_opy_[bstack1ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭৆")]):
                bstack1llll1l1l_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack1111l11l_opy_,
                                                            args=(self.bstack1111ll11_opy_, bstack1111111l_opy_, bstack11l1l11l_opy_)))
            bstack111ll1l1_opy_ = len(self.bstack111l1111_opy_[bstack1ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧে")])
        else:
            bstack1llll1l1l_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack1111l11l_opy_,
                                                        args=(self.bstack1111ll11_opy_, bstack1111111l_opy_, bstack11l1l11l_opy_)))
            bstack111ll1l1_opy_ = 1
        i = 0
        for t in bstack1llll1l1l_opy_:
            os.environ[bstack1ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬৈ")] = str(i)
            if bstack1ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ৉") in self.bstack111l1111_opy_:
                os.environ[bstack1ll1l_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨ৊")] = json.dumps(self.bstack111l1111_opy_[bstack1ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫো")][i % bstack111ll1l1_opy_])
            i += 1
            t.start()
        for t in bstack1llll1l1l_opy_:
            t.join()
        return list(bstack11l1l11l_opy_)
    @staticmethod
    def bstack1111l1ll_opy_(driver, bstack111l11l1_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack1ll1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭ৌ"), None)
        if item and getattr(item, bstack1ll1l_opy_ (u"ࠪࡣࡦ࠷࠱ࡺࡡࡷࡩࡸࡺ࡟ࡤࡣࡶࡩ্ࠬ"), None) and not getattr(item, bstack1ll1l_opy_ (u"ࠫࡤࡧ࠱࠲ࡻࡢࡷࡹࡵࡰࡠࡦࡲࡲࡪ࠭ৎ"), False):
            logger.info(
                bstack1ll1l_opy_ (u"ࠧࡇࡵࡵࡱࡰࡥࡹ࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡳࡳࠦࡨࡢࡵࠣࡩࡳࡪࡥࡥ࠰ࠣࡔࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡧࡱࡵࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡹ࡫ࡳࡵ࡫ࡱ࡫ࠥ࡯ࡳࠡࡷࡱࡨࡪࡸࡷࡢࡻ࠱ࠦ৏"))
            bstack111lll1l_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1lllllll1_opy_.bstack1lllll111_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack111l1l1l_opy_(self):
        bstack1ll1l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶࠤࡹ࡮ࡥࠡ࡮࡬ࡷࡹࠦ࡯ࡧࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡴࡰࠢࡥࡩࠥ࡫ࡸࡦࡥࡸࡸࡪࡪࠠࡣࡻࠣࡴࡦࡸࡳࡪࡰࡪࠤࡹ࡮ࡥࠡࡱࡸࡸࡵࡻࡴࠡࡱࡩࠤࡵࡿࡴࡦࡵࡷࠤ࠲࠳ࡣࡰ࡮࡯ࡩࡨࡺ࠭ࡰࡰ࡯ࡽ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡏࡱࡷࡩ࠿ࠦࡔࡩࡧࠣࡶࡪ࡭ࡥࡹࠢࡳࡥࡹࡺࡥࡳࡰࠣࡹࡸ࡫ࡤࠡࡪࡨࡶࡪࠦࡤࡦࡲࡨࡲࡩࡹࠠࡰࡰࠣࡴࡾࡺࡥࡴࡶࠪࡷࠥࡵࡵࡵࡲࡸࡸࠥ࡬࡯ࡳ࡯ࡤࡸࠥ࡬࡯ࡳࠢ࠿ࡑࡴࡪࡵ࡭ࡧࠣ࠲࠳࠴࠾ࠡ࡮࡬ࡲࡪࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧ৐")
        try:
            bstack1llllll11_opy_ = [bstack1ll1l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺࠢ৑"), *self.bstack1111ll11_opy_, bstack1ll1l_opy_ (u"ࠣ࠯࠰ࡧࡴࡲ࡬ࡦࡥࡷ࠱ࡴࡴ࡬ࡺࠤ৒")]
            result = subprocess.run(bstack1llllll11_opy_, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.stderr:
                self.logger.info(bstack1ll1l_opy_ (u"ࠤ࡚ࡥࡷࡴࡩ࡯ࡩࡶࠤࡩࡻࡲࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤ৓").format(result.stderr))
            if result.returncode != 0 and not result.stdout:
                self.logger.error(bstack1ll1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࡶࠤ࡫࡯࡬ࡦ࠼ࠣࡿࢂࠨ৔").format(result.stderr))
                return []
            self.logger.info(bstack1ll1l_opy_ (u"ࠦࡈࡵ࡬࡭ࡧࡦࡸࡪࡪࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡺࡹࡩ࡯ࡩࠣࡴࡾࡺࡥࡴࡶࠣ࠾ࠥࢁࡽࠣ৕").format(result.stdout))
            file_names = set(re.findall(self.bstack1lll1lll1_opy_, result.stdout))
            file_names = sorted(file_names)
            return list(file_names)
        except Exception as e:
            self.logger.error(bstack1lllll1l1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳ࠻ࠢࡾࡩࢂࠨ৖"))
            return []