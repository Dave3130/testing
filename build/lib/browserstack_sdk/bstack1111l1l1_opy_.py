# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack11111ll1_opy_
import subprocess
import re
from browserstack_sdk.bstack1llll11l1_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack11111111_opy_
from bstack_utils.bstack1111l11l_opy_ import bstack11111l1l_opy_
from bstack_utils.constants import bstack111l11ll_opy_
from bstack_utils.bstack1llll111l_opy_ import bstack11111l11_opy_
class bstack111111l1_opy_:
    def __init__(self, args, logger, bstack111l1l1l_opy_, bstack1111llll_opy_):
        self.args = args
        self.logger = logger
        self.bstack111l1l1l_opy_ = bstack111l1l1l_opy_
        self.bstack1111llll_opy_ = bstack1111llll_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack11l11l1l_opy_ = []
        self.bstack111ll111_opy_ = []
        self.bstack1111ll11_opy_ = []
        self.bstack1lllll11l_opy_ = self.bstack1lll1llll_opy_()
        self.bstack11l11l11_opy_ = -1
    def bstack1lllll1l1_opy_(self, bstack111ll1l1_opy_):
        self.parse_args()
        self.bstack11l1111l_opy_()
        self.bstack11l11111_opy_(bstack111ll1l1_opy_)
        self.bstack111l1111_opy_()
    def bstack111ll1ll_opy_(self):
        bstack1llll111l_opy_ = bstack11111l11_opy_.bstack1llll11ll_opy_(self.bstack111l1l1l_opy_, self.logger)
        if bstack1llll111l_opy_ is None:
            self.logger.warn(bstack1l_opy_ (u"ࠢࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡩࡣࡱࡨࡱ࡫ࡲࠡ࡫ࡶࠤࡳࡵࡴࠡ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩࡩ࠴ࠠࡔ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥ঒"))
            return
        bstack11l111ll_opy_ = False
        bstack1llll111l_opy_.bstack1lll1lll1_opy_(bstack1l_opy_ (u"ࠣࡧࡱࡥࡧࡲࡥࡥࠤও"), bstack1llll111l_opy_.bstack111lll11_opy_())
        start_time = time.time()
        if bstack1llll111l_opy_.bstack111lll11_opy_():
            test_files = self.bstack111111ll_opy_()
            bstack11l111ll_opy_ = True
            bstack1lllll1ll_opy_ = bstack1llll111l_opy_.bstack1111lll1_opy_(test_files)
            if bstack1lllll1ll_opy_:
                self.bstack11l11l1l_opy_ = [os.path.normpath(item).replace(bstack1l_opy_ (u"ࠩ࡟ࡠࠬঔ"), bstack1l_opy_ (u"ࠪ࠳ࠬক")) for item in bstack1lllll1ll_opy_]
                self.__1llll1lll_opy_()
                bstack1llll111l_opy_.bstack11111lll_opy_(bstack11l111ll_opy_)
                self.logger.info(bstack1l_opy_ (u"࡙ࠦ࡫ࡳࡵࡵࠣࡶࡪࡵࡲࡥࡧࡵࡩࡩࠦࡵࡴ࡫ࡱ࡫ࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤখ").format(self.bstack11l11l1l_opy_))
            else:
                self.logger.info(bstack1l_opy_ (u"ࠧࡔ࡯ࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡽࡥࡳࡧࠣࡶࡪࡵࡲࡥࡧࡵࡩࡩࠦࡢࡺࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥগ"))
        bstack1llll111l_opy_.bstack1lll1lll1_opy_(bstack1l_opy_ (u"ࠨࡴࡪ࡯ࡨࡘࡦࡱࡥ࡯ࡖࡲࡅࡵࡶ࡬ࡺࠤঘ"), int((time.time() - start_time) * 1000)) # bstack1lllllll1_opy_ to bstack111lll1l_opy_
    def __1llll1lll_opy_(self):
        bstack1l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡋࡵࡲࠡࡧࡤࡧ࡭ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࠢ࡬ࡲࠥࡹࡥ࡭ࡨ࠱ࡷࡵ࡫ࡣࡠࡨ࡬ࡰࡪࡹࠬࠡࡥࡲࡰࡱ࡫ࡣࡵࠢࡤࡰࡱࠦ࡮ࡰࡦࡨ࡭ࡩࡹࠠࡶࡵ࡬ࡲ࡬ࠦࡰࡺࡶࡨࡷࡹࠦ࠭࠮ࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡲࡲࡱࡿࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦঙ")
        bstack1111l111_opy_ = []
        for bstack11l1l11l_opy_ in self.bstack11l11l1l_opy_:
            try:
                bstack111l1l11_opy_ = [bstack1l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣচ"), bstack11l1l11l_opy_, bstack1l_opy_ (u"ࠤ࠰࠱ࡨࡵ࡬࡭ࡧࡦࡸ࠲ࡵ࡮࡭ࡻࠥছ"), bstack1l_opy_ (u"ࠥ࠱ࡶࠨজ")]
                result = subprocess.run(bstack111l1l11_opy_, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=60)
                if result.returncode != 0 and result.stdout:
                    self.logger.error(bstack1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡳ࡭ࠠ࡯ࡱࡧࡩࠥ࡯ࡤࠡࡨࡲࡶࠥࢁࡽ࠻ࠢࡾࢁࠧঝ").format(bstack11l1l11l_opy_, result.stderr))
                    continue
                for line in result.stdout.splitlines():
                    line = line.strip()
                    if line and not line.startswith(bstack1l_opy_ (u"ࠧࡂࠢঞ")) and bstack1l_opy_ (u"ࠨ࠺࠻ࠤট") in line:
                        bstack1111l111_opy_.append(line)
            except subprocess.TimeoutExpired:
                self.logger.error(bstack1l_opy_ (u"ࠢࡏࡱࡧࡩࠥࡏࡤࠡࡵࡨࡰࡪࡩࡴࡪࡱࡱࠤࡹ࡯࡭ࡦࡦࠣࡳࡺࡺࠠࡧࡱࡵࠤࢀࢃࠢঠ").format(bstack11l1l11l_opy_))
                return 0
            except Exception as e:
                self.logger.error(bstack1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡳࡵࡤࡦࠢ࡬ࡨࠥ࡬࡯ࡳࠢࡩ࡭ࡱ࡫࠺ࠡࡽࢀࠦড").format(bstack11l1l11l_opy_))
                return 0
        os.environ[bstack1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡑࡕࡇࡍࡋࡓࡕࡔࡄࡘࡊࡊ࡟ࡔࡇࡏࡉࡈ࡚ࡏࡓࡕࠪঢ")] = json.dumps(bstack1111l111_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack111ll11l_opy_():
        import importlib
        if getattr(importlib, bstack1l_opy_ (u"ࠪࡪ࡮ࡴࡤࡠ࡮ࡲࡥࡩ࡫ࡲࠨণ"), False):
            bstack111l1lll_opy_ = importlib.find_loader(bstack1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭ত"))
        else:
            bstack111l1lll_opy_ = importlib.util.find_spec(bstack1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧথ"))
    def bstack1llll1l1l_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack11l11l11_opy_ = -1
        if self.bstack1111llll_opy_ and bstack1l_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭দ") in self.bstack111l1l1l_opy_:
            self.bstack11l11l11_opy_ = int(self.bstack111l1l1l_opy_[bstack1l_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧধ")])
        try:
            bstack1llll1111_opy_ = [bstack1l_opy_ (u"ࠨ࠯࠰ࡨࡷ࡯ࡶࡦࡴࠪন"), bstack1l_opy_ (u"ࠩ࠰࠱ࡵࡲࡵࡨ࡫ࡱࡷࠬ঩"), bstack1l_opy_ (u"ࠪ࠱ࡵ࠭প")]
            if self.bstack11l11l11_opy_ >= 0:
                bstack1llll1111_opy_.extend([bstack1l_opy_ (u"ࠫ࠲࠳࡮ࡶ࡯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬফ"), bstack1l_opy_ (u"ࠬ࠳࡮ࠨব")])
            for arg in bstack1llll1111_opy_:
                self.bstack1llll1l1l_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack11l1111l_opy_(self):
        bstack111ll111_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack111ll111_opy_ = bstack111ll111_opy_
        return self.bstack111ll111_opy_
    def bstack111l11l1_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack111ll11l_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack11111111_opy_)
    def bstack11l11111_opy_(self, bstack111ll1l1_opy_):
        bstack1lll1ll1l_opy_ = Config.bstack1llll11ll_opy_()
        if bstack111ll1l1_opy_:
            self.bstack111ll111_opy_.append(bstack1l_opy_ (u"࠭࠭࠮ࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪভ"))
            self.bstack111ll111_opy_.append(bstack1l_opy_ (u"ࠧࡕࡴࡸࡩࠬম"))
        if bstack1lll1ll1l_opy_.bstack1llll1l11_opy_():
            self.bstack111ll111_opy_.append(bstack1l_opy_ (u"ࠨ࠯࠰ࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧয"))
            self.bstack111ll111_opy_.append(bstack1l_opy_ (u"ࠩࡗࡶࡺ࡫ࠧর"))
        self.bstack111ll111_opy_.append(bstack1l_opy_ (u"ࠪ࠱ࡵ࠭঱"))
        self.bstack111ll111_opy_.append(bstack1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡳࡰࡺ࡭ࡩ࡯ࠩল"))
        self.bstack111ll111_opy_.append(bstack1l_opy_ (u"ࠬ࠳࠭ࡥࡴ࡬ࡺࡪࡸࠧ঳"))
        self.bstack111ll111_opy_.append(bstack1l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭঴"))
        if self.bstack11l11l11_opy_ > 1:
            self.bstack111ll111_opy_.append(bstack1l_opy_ (u"ࠧ࠮ࡰࠪ঵"))
            self.bstack111ll111_opy_.append(str(self.bstack11l11l11_opy_))
    def bstack111l1111_opy_(self):
        if bstack11111l1l_opy_.bstack1llllll11_opy_(self.bstack111l1l1l_opy_):
             self.bstack111ll111_opy_ += [
                bstack111l11ll_opy_.get(bstack1l_opy_ (u"ࠨࡴࡨࡶࡺࡴࠧশ")), str(bstack11111l1l_opy_.bstack1111l1ll_opy_(self.bstack111l1l1l_opy_)),
                bstack111l11ll_opy_.get(bstack1l_opy_ (u"ࠩࡧࡩࡱࡧࡹࠨষ")), str(bstack111l11ll_opy_.get(bstack1l_opy_ (u"ࠪࡶࡪࡸࡵ࡯࠯ࡧࡩࡱࡧࡹࠨস")))
            ]
    def bstack1111ll1l_opy_(self):
        bstack1111ll11_opy_ = []
        for spec in self.bstack11l11l1l_opy_:
            bstack1llll1ll1_opy_ = [spec]
            bstack1llll1ll1_opy_ += self.bstack111ll111_opy_
            bstack1111ll11_opy_.append(bstack1llll1ll1_opy_)
        self.bstack1111ll11_opy_ = bstack1111ll11_opy_
        return bstack1111ll11_opy_
    def bstack1lll1llll_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack1lllll11l_opy_ = True
            return True
        except Exception as e:
            self.bstack1lllll11l_opy_ = False
        return self.bstack1lllll11l_opy_
    def bstack111lllll_opy_(self):
        bstack1l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡍࡥࡵࠢࡷ࡬ࡪࠦࡣࡰࡷࡱࡸࠥࡵࡦࠡࡶࡨࡷࡹࡹࠠࡸ࡫ࡷ࡬ࡴࡻࡴࠡࡴࡸࡲࡳ࡯࡮ࡨࠢࡷ࡬ࡪࡳࠠࡶࡵ࡬ࡲ࡬ࠦࡰࡺࡶࡨࡷࡹ࠭ࡳࠡ࠯࠰ࡧࡴࡲ࡬ࡦࡥࡷ࠱ࡴࡴ࡬ࡺࠢࡩࡰࡦ࡭࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࡭ࡳࡺ࠺ࠡࡖ࡫ࡩࠥࡺ࡯ࡵࡣ࡯ࠤࡳࡻ࡭ࡣࡧࡵࠤࡴ࡬ࠠࡵࡧࡶࡸࡸࠦࡣࡰ࡮࡯ࡩࡨࡺࡥࡥ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢহ")
        try:
            self.logger.info(bstack1l_opy_ (u"ࠧࡉ࡯࡭࡮ࡨࡧࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࡳࠡࡷࡶ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠠ࠮࠯ࡦࡳࡱࡲࡥࡤࡶ࠰ࡳࡳࡲࡹࠣ঺"))
            bstack111l1l11_opy_ = [bstack1l_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࠨ঻"), *self.bstack111ll111_opy_, bstack1l_opy_ (u"ࠢ࠮࠯ࡦࡳࡱࡲࡥࡤࡶ࠰ࡳࡳࡲࡹ়ࠣ"), bstack1l_opy_ (u"ࠣ࠯ࡴࠦঽ")]
            result = subprocess.run(
                bstack111l1l11_opy_,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=60
            )
            if result.returncode not in (0, 5) and result.stdout:
                self.logger.error(bstack1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࡵ࠽ࠤࢀࢃࠢা").format(result.stderr))
                return 0
            test_count = 0
            for line in result.stdout.splitlines():
                line = line.strip()
                if line and bstack1l_opy_ (u"ࠪ࠾࠿࠭ি") in line and not line.startswith(bstack1l_opy_ (u"ࠫࡁ࠭ী")) and not line.endswith(bstack1l_opy_ (u"ࠬࡩ࡯࡭࡮ࡨࡧࡹ࡫ࡤࠨু")):
                    test_count += 1
            self.logger.info(bstack1l_opy_ (u"ࠨࡔࡰࡶࡤࡰࠥࡺࡥࡴࡶࡶࠤࡨࡵ࡬࡭ࡧࡦࡸࡪࡪ࠺ࠡࡽࢀࠦূ").format(test_count))
            return test_count
        except subprocess.TimeoutExpired:
            self.logger.error(bstack1l_opy_ (u"ࠢࡕࡧࡶࡸࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯ࠢࡷ࡭ࡲ࡫ࡤࠡࡱࡸࡸࠧৃ"))
            return 0
        except Exception as e:
            self.logger.error(bstack1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡦࡳࡺࡴࡴ࠻ࠢࡾࢁࠧৄ").format(e))
            return 0
    def bstack11l11ll1_opy_(self, bstack11l11lll_opy_, bstack1lllll1l1_opy_):
        bstack1lllll1l1_opy_[bstack1l_opy_ (u"ࠩࡆࡓࡓࡌࡉࡈࠩ৅")] = self.bstack111l1l1l_opy_
        multiprocessing.set_start_method(bstack1l_opy_ (u"ࠪࡷࡵࡧࡷ࡯ࠩ৆"))
        bstack1111111l_opy_ = []
        manager = multiprocessing.Manager()
        bstack111llll1_opy_ = manager.list()
        if bstack1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧে") in self.bstack111l1l1l_opy_:
            for index, platform in enumerate(self.bstack111l1l1l_opy_[bstack1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨৈ")]):
                bstack1111111l_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack11l11lll_opy_,
                                                            args=(self.bstack111ll111_opy_, bstack1lllll1l1_opy_, bstack111llll1_opy_)))
            bstack11l111l1_opy_ = len(self.bstack111l1l1l_opy_[bstack1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ৉")])
        else:
            bstack1111111l_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack11l11lll_opy_,
                                                        args=(self.bstack111ll111_opy_, bstack1lllll1l1_opy_, bstack111llll1_opy_)))
            bstack11l111l1_opy_ = 1
        i = 0
        for t in bstack1111111l_opy_:
            os.environ[bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧ৊")] = str(i)
            if bstack1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫো") in self.bstack111l1l1l_opy_:
                os.environ[bstack1l_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪৌ")] = json.dumps(self.bstack111l1l1l_opy_[bstack1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ্࠭")][i % bstack11l111l1_opy_])
            i += 1
            t.start()
        for t in bstack1111111l_opy_:
            t.join()
        return list(bstack111llll1_opy_)
    @staticmethod
    def bstack1llllll1l_opy_(driver, bstack111l111l_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨৎ"), None)
        if item and getattr(item, bstack1l_opy_ (u"ࠬࡥࡡ࠲࠳ࡼࡣࡹ࡫ࡳࡵࡡࡦࡥࡸ࡫ࠧ৏"), None) and not getattr(item, bstack1l_opy_ (u"࠭࡟ࡢ࠳࠴ࡽࡤࡹࡴࡰࡲࡢࡨࡴࡴࡥࠨ৐"), False):
            logger.info(
                bstack1l_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠥࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡪࡵࠣࡹࡳࡪࡥࡳࡹࡤࡽ࠳ࠨ৑"))
            bstack11l1l111_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack11111ll1_opy_.bstack111l1ll1_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack111111ll_opy_(self):
        bstack1l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࠦࡴࡩࡧࠣࡰ࡮ࡹࡴࠡࡱࡩࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡶࡲࠤࡧ࡫ࠠࡦࡺࡨࡧࡺࡺࡥࡥࠢࡥࡽࠥࡶࡡࡳࡵ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡳࡺࡺࡰࡶࡶࠣࡳ࡫ࠦࡰࡺࡶࡨࡷࡹࠦ࠭࠮ࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡲࡲࡱࡿ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧ৒")
        try:
            bstack111l1l11_opy_ = [
                bstack1l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵࠤ৓"),
                *self.bstack111ll111_opy_,
                bstack1l_opy_ (u"ࠥ࠱࠲ࡩ࡯࡭࡮ࡨࡧࡹ࠳࡯࡯࡮ࡼࠦ৔"),
                bstack1l_opy_ (u"ࠦ࠲ࡷࠢ৕")  # bstack1llllllll_opy_ mode for bstack1lllll111_opy_ output
            ]
            result = subprocess.run(
                bstack111l1l11_opy_,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=60
            )
            if result.returncode not in (0, 5) and result.stdout:
                self.logger.error(bstack1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࡸࠦࡦࡪ࡮ࡨ࠾ࠥࢁࡽࠨ৖").format(result.stderr))
                return []
            file_paths = set()
            for line in result.stdout.splitlines():
                line = line.strip()
                if line and bstack1l_opy_ (u"࠭࠺࠻ࠩৗ") in line and not line.startswith(bstack1l_opy_ (u"ࠧ࠽ࠩ৘")):
                    file_path = line.split(bstack1l_opy_ (u"ࠨ࠼࠽ࠫ৙"), 1)[0]
                    if file_path.endswith(bstack1l_opy_ (u"ࠩ࠱ࡴࡾ࠭৚")):
                        file_paths.add(file_path)
            test_files = sorted(file_paths)
            if test_files:
                self.logger.debug(bstack1l_opy_ (u"ࠥࡇࡴࡲ࡬ࡦࡥࡷࡩࡩࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵ࠽ࠤࢀࢃࠢ৛").format(len(test_files)))
            elif result.returncode == 5:
                self.logger.debug(bstack1l_opy_ (u"ࠦࡓࡵࠠࡵࡧࡶࡸࡸࠦࡦࡪ࡮ࡨࡷࠥࡩ࡯࡭࡮ࡨࡧࡹ࡫ࡤࠣড়"))
            return test_files
        except subprocess.TimeoutExpired:
            self.logger.error(bstack1l_opy_ (u"࡚ࠧࡥࡴࡶࠣࡊ࡮ࡲࡥࡴࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࠦࡴࡪ࡯ࡨࡨࠥࡵࡵࡵࠤঢ়"))
            return []
        except Exception as e:
            self.logger.error(bstack1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯࠼ࠣࡿࢂࠨ৞").format(e))
            return []