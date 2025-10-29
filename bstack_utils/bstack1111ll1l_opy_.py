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
import os
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack11ll1l1l111_opy_ import bstack11ll1l11ll1_opy_
from bstack_utils.bstack1llll1l1l_opy_ import bstack111ll11l_opy_
from bstack_utils.helper import bstack11lll1l11_opy_
import json
class bstack1lll1111l_opy_:
    _1ll1l1ll1ll_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack11111ll1ll1_opy_ = bstack11ll1l11ll1_opy_(self.config, logger)
        self.bstack1llll1l1l_opy_ = bstack111ll11l_opy_.bstack1llll111l_opy_(config=self.config)
        self.bstack11111llll1l_opy_ = {}
        self.bstack1llllll11_opy_ = False
        self.bstack11111lll1l1_opy_ = (
            self.__11111ll1l1l_opy_()
            and self.bstack1llll1l1l_opy_ is not None
            and self.bstack1llll1l1l_opy_.bstack1lll1ll1l_opy_()
            and config.get(bstack11l11ll_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨỆ"), None) is not None
            and config.get(bstack11l11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧệ"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack1llll111l_opy_(cls, config, logger):
        if cls._1ll1l1ll1ll_opy_ is None and config is not None:
            cls._1ll1l1ll1ll_opy_ = bstack1lll1111l_opy_(config, logger)
        return cls._1ll1l1ll1ll_opy_
    def bstack1lll1ll1l_opy_(self):
        bstack11l11ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡇࡳࠥࡴ࡯ࡵࠢࡤࡴࡵࡲࡹࠡࡶࡨࡷࡹࠦ࡯ࡳࡦࡨࡶ࡮ࡴࡧࠡࡹ࡫ࡩࡳࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡕ࠱࠲ࡻࠣ࡭ࡸࠦ࡮ࡰࡶࠣࡩࡳࡧࡢ࡭ࡧࡧࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡒࡶࡩ࡫ࡲࡪࡰࡪࠤ࡮ࡹࠠ࡯ࡱࡷࠤࡪࡴࡡࡣ࡮ࡨࡨࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠡ࡫ࡶࠤࡓࡵ࡮ࡦࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠣ࡭ࡸࠦࡎࡰࡰࡨࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣỈ")
        return self.bstack11111lll1l1_opy_ and self.bstack11111lll11l_opy_()
    def bstack11111lll11l_opy_(self):
        bstack11111lll111_opy_ = os.getenv(bstack11l11ll_opy_ (u"࠭ࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࡡࡘࡗࡊࡊࠧỉ"), self.config.get(bstack11l11ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪỊ"), None))
        return bstack11111lll111_opy_ in bstack11l11llll11_opy_
    def __11111ll1l1l_opy_(self):
        bstack11ll11l1lll_opy_ = False
        for fw in bstack11l1l1111ll_opy_:
            if fw in self.config.get(bstack11l11ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫị"), bstack11l11ll_opy_ (u"ࠩࠪỌ")):
                bstack11ll11l1lll_opy_ = True
        return bstack11lll1l11_opy_(self.config.get(bstack11l11ll_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧọ"), bstack11ll11l1lll_opy_))
    def bstack11111llll11_opy_(self):
        return (not self.bstack1lll1ll1l_opy_() and
                self.bstack1llll1l1l_opy_ is not None and self.bstack1llll1l1l_opy_.bstack1lll1ll1l_opy_())
    def bstack11111lllll1_opy_(self):
        if not self.bstack11111llll11_opy_():
            return
        if self.config.get(bstack11l11ll_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩỎ"), None) is None or self.config.get(bstack11l11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨỏ"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack11l11ll_opy_ (u"ࠨࡔࡦࡵࡷࠤࡗ࡫࡯ࡳࡦࡨࡶ࡮ࡴࡧࠡࡥࡤࡲࠬࡺࠠࡸࡱࡵ࡯ࠥࡧࡳࠡࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠤࡴࡸࠠࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠥ࡯ࡳࠡࡰࡸࡰࡱ࠴ࠠࡑ࡮ࡨࡥࡸ࡫ࠠࡴࡧࡷࠤࡦࠦ࡮ࡰࡰ࠰ࡲࡺࡲ࡬ࠡࡸࡤࡰࡺ࡫࠮ࠣỐ"))
        if not self.__11111ll1l1l_opy_():
            self.logger.info(bstack11l11ll_opy_ (u"ࠢࡕࡧࡶࡸࠥࡘࡥࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡦࡥࡳ࠭ࡴࠡࡹࡲࡶࡰࠦࡡࡴࠢࡷࡩࡸࡺࡒࡦࡲࡲࡶࡹ࡯࡮ࡨࠢ࡬ࡷࠥࡪࡩࡴࡣࡥࡰࡪࡪ࠮ࠡࡒ࡯ࡩࡦࡹࡥࠡࡧࡱࡥࡧࡲࡥࠡ࡫ࡷࠤ࡫ࡸ࡯࡮ࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠥ࡬ࡩ࡭ࡧ࠱ࠦố"))
    def bstack11111lll1ll_opy_(self):
        return self.bstack1llllll11_opy_
    def bstack1lll11l11_opy_(self, bstack11111ll1lll_opy_):
        self.bstack1llllll11_opy_ = bstack11111ll1lll_opy_
        self.bstack1lll111ll_opy_(bstack11l11ll_opy_ (u"ࠣࡣࡳࡴࡱ࡯ࡥࡥࠤỒ"), bstack11111ll1lll_opy_)
    def bstack111111l1_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack11l11ll_opy_ (u"ࠤ࡞ࡶࡪࡵࡲࡥࡧࡵࡣࡹ࡫ࡳࡵࡡࡩ࡭ࡱ࡫ࡳ࡞ࠢࡑࡳࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴࠢࡳࡶࡴࡼࡩࡥࡧࡧࠤ࡫ࡵࡲࠡࡱࡵࡨࡪࡸࡩ࡯ࡩ࠱ࠦồ"))
                return None
            orchestration_strategy = None
            orchestration_metadata = self.bstack1llll1l1l_opy_.bstack111ll1lllll_opy_()
            if self.bstack1llll1l1l_opy_ is not None:
                orchestration_strategy = self.bstack1llll1l1l_opy_.bstack11l1l11l11_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack11l11ll_opy_ (u"ࠥࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡷࡹࡸࡡࡵࡧࡪࡽࠥ࡯ࡳࠡࡐࡲࡲࡪ࠴ࠠࡄࡣࡱࡲࡴࡺࠠࡱࡴࡲࡧࡪ࡫ࡤࠡࡹ࡬ࡸ࡭ࠦࡴࡦࡵࡷࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠳ࠨỔ"))
                return None
            self.logger.info(bstack11l11ll_opy_ (u"ࠦࡗ࡫࡯ࡳࡦࡨࡶ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡽࡩࡵࡪࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡷࡹࡸࡡࡵࡧࡪࡽ࠿ࠦࡻࡾࠤổ").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack11l11ll_opy_ (u"࡛ࠧࡳࡪࡰࡪࠤࡈࡒࡉࠡࡨ࡯ࡳࡼࠦࡦࡰࡴࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴ࠮ࠣỖ"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy, json.dumps(orchestration_metadata))
            else:
                self.logger.debug(bstack11l11ll_opy_ (u"ࠨࡕࡴ࡫ࡱ࡫ࠥࡹࡤ࡬ࠢࡩࡰࡴࡽࠠࡧࡱࡵࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠯ࠤỗ"))
                self.bstack11111ll1ll1_opy_.bstack11ll1lll11l_opy_(test_files, orchestration_strategy, orchestration_metadata)
                ordered_test_files = self.bstack11111ll1ll1_opy_.bstack11ll1lll1ll_opy_()
            if not ordered_test_files:
                return None
            self.bstack1lll111ll_opy_(bstack11l11ll_opy_ (u"ࠢࡶࡲ࡯ࡳࡦࡪࡥࡥࡖࡨࡷࡹࡌࡩ࡭ࡧࡶࡇࡴࡻ࡮ࡵࠤỘ"), len(test_files))
            self.bstack1lll111ll_opy_(bstack11l11ll_opy_ (u"ࠣࡰࡲࡨࡪࡏ࡮ࡥࡧࡻࠦộ"), int(os.environ.get(bstack11l11ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡐࡒࡈࡊࡥࡉࡏࡆࡈ࡜ࠧỚ")) or bstack11l11ll_opy_ (u"ࠥ࠴ࠧớ")))
            self.bstack1lll111ll_opy_(bstack11l11ll_opy_ (u"ࠦࡹࡵࡴࡢ࡮ࡑࡳࡩ࡫ࡳࠣỜ"), int(os.environ.get(bstack11l11ll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡓࡕࡄࡆࡡࡆࡓ࡚ࡔࡔࠣờ")) or bstack11l11ll_opy_ (u"ࠨ࠱ࠣỞ")))
            self.bstack1lll111ll_opy_(bstack11l11ll_opy_ (u"ࠢࡥࡱࡺࡲࡱࡵࡡࡥࡧࡧࡘࡪࡹࡴࡇ࡫࡯ࡩࡸࡉ࡯ࡶࡰࡷࠦở"), len(ordered_test_files))
            self.bstack1lll111ll_opy_(bstack11l11ll_opy_ (u"ࠣࡵࡳࡰ࡮ࡺࡔࡦࡵࡷࡷࡆࡖࡉࡄࡣ࡯ࡰࡈࡵࡵ࡯ࡶࠥỠ"), self.bstack11111ll1ll1_opy_.bstack11ll1llllll_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack11l11ll_opy_ (u"ࠤ࡞ࡶࡪࡵࡲࡥࡧࡵࡣࡹ࡫ࡳࡵࡡࡩ࡭ࡱ࡫ࡳ࡞ࠢࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡴࡸࡤࡦࡴ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡲࡡࡴࡵࡨࡷ࠿ࠦࡻࡾࠤỡ").format(e))
        return None
    def bstack1lll111ll_opy_(self, key, value):
        self.bstack11111llll1l_opy_[key] = value
    def bstack1111ll1lll_opy_(self):
        return self.bstack11111llll1l_opy_