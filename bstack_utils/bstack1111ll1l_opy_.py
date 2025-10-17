# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
import os
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack11ll1ll1lll_opy_ import bstack11ll1ll1l1l_opy_
from bstack_utils.bstack111ll11l_opy_ import bstack1lllll1ll_opy_
from bstack_utils.helper import bstack1l11111l1l_opy_
import json
class bstack1111l11l_opy_:
    _1ll1ll111ll_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack1111l1111ll_opy_ = bstack11ll1ll1l1l_opy_(self.config, logger)
        self.bstack111ll11l_opy_ = bstack1lllll1ll_opy_.bstack111111ll_opy_(config=self.config)
        self.bstack1111l111l11_opy_ = {}
        self.bstack11111ll1_opy_ = False
        self.bstack1111l111ll1_opy_ = (
            self.__1111l11l11l_opy_()
            and self.bstack111ll11l_opy_ is not None
            and self.bstack111ll11l_opy_.bstack1llll1111_opy_()
            and config.get(bstack11111_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨṹ"), None) is not None
            and config.get(bstack11111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧṺ"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack111111ll_opy_(cls, config, logger):
        if cls._1ll1ll111ll_opy_ is None and config is not None:
            cls._1ll1ll111ll_opy_ = bstack1111l11l_opy_(config, logger)
        return cls._1ll1ll111ll_opy_
    def bstack1llll1111_opy_(self):
        bstack11111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡇࡳࠥࡴ࡯ࡵࠢࡤࡴࡵࡲࡹࠡࡶࡨࡷࡹࠦ࡯ࡳࡦࡨࡶ࡮ࡴࡧࠡࡹ࡫ࡩࡳࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡕ࠱࠲ࡻࠣ࡭ࡸࠦ࡮ࡰࡶࠣࡩࡳࡧࡢ࡭ࡧࡧࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡒࡶࡩ࡫ࡲࡪࡰࡪࠤ࡮ࡹࠠ࡯ࡱࡷࠤࡪࡴࡡࡣ࡮ࡨࡨࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠡ࡫ࡶࠤࡓࡵ࡮ࡦࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠣ࡭ࡸࠦࡎࡰࡰࡨࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣṻ")
        return self.bstack1111l111ll1_opy_ and self.bstack1111l1111l1_opy_()
    def bstack1111l1111l1_opy_(self):
        bstack1111l11l111_opy_ = os.getenv(bstack11111_opy_ (u"࠭ࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࡡࡘࡗࡊࡊࠧṼ"), self.config.get(bstack11111_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪṽ"), None))
        return bstack1111l11l111_opy_ in bstack11l11ll1lll_opy_
    def __1111l11l11l_opy_(self):
        bstack11ll1l111ll_opy_ = False
        for fw in bstack11l1l1111l1_opy_:
            if fw in self.config.get(bstack11111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫṾ"), bstack11111_opy_ (u"ࠩࠪṿ")):
                bstack11ll1l111ll_opy_ = True
        return bstack1l11111l1l_opy_(self.config.get(bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧẀ"), bstack11ll1l111ll_opy_))
    def bstack1111l111lll_opy_(self):
        return (not self.bstack1llll1111_opy_() and
                self.bstack111ll11l_opy_ is not None and self.bstack111ll11l_opy_.bstack1llll1111_opy_())
    def bstack1111l111l1l_opy_(self):
        if not self.bstack1111l111lll_opy_():
            return
        if self.config.get(bstack11111_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩẁ"), None) is None or self.config.get(bstack11111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨẂ"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack11111_opy_ (u"ࠨࡔࡦࡵࡷࠤࡗ࡫࡯ࡳࡦࡨࡶ࡮ࡴࡧࠡࡥࡤࡲࠬࡺࠠࡸࡱࡵ࡯ࠥࡧࡳࠡࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠤࡴࡸࠠࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠥ࡯ࡳࠡࡰࡸࡰࡱ࠴ࠠࡑ࡮ࡨࡥࡸ࡫ࠠࡴࡧࡷࠤࡦࠦ࡮ࡰࡰ࠰ࡲࡺࡲ࡬ࠡࡸࡤࡰࡺ࡫࠮ࠣẃ"))
        if not self.__1111l11l11l_opy_():
            self.logger.info(bstack11111_opy_ (u"ࠢࡕࡧࡶࡸࠥࡘࡥࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡦࡥࡳ࠭ࡴࠡࡹࡲࡶࡰࠦࡡࡴࠢࡷࡩࡸࡺࡒࡦࡲࡲࡶࡹ࡯࡮ࡨࠢ࡬ࡷࠥࡪࡩࡴࡣࡥࡰࡪࡪ࠮ࠡࡒ࡯ࡩࡦࡹࡥࠡࡧࡱࡥࡧࡲࡥࠡ࡫ࡷࠤ࡫ࡸ࡯࡮ࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠥ࡬ࡩ࡭ࡧ࠱ࠦẄ"))
    def bstack1111l11111l_opy_(self):
        return self.bstack11111ll1_opy_
    def bstack111111l1_opy_(self, bstack1111l11l1l1_opy_):
        self.bstack11111ll1_opy_ = bstack1111l11l1l1_opy_
        self.bstack111l1l1l_opy_(bstack11111_opy_ (u"ࠣࡣࡳࡴࡱ࡯ࡥࡥࠤẅ"), bstack1111l11l1l1_opy_)
    def bstack111l11ll_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack11111_opy_ (u"ࠤ࡞ࡶࡪࡵࡲࡥࡧࡵࡣࡹ࡫ࡳࡵࡡࡩ࡭ࡱ࡫ࡳ࡞ࠢࡑࡳࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴࠢࡳࡶࡴࡼࡩࡥࡧࡧࠤ࡫ࡵࡲࠡࡱࡵࡨࡪࡸࡩ࡯ࡩ࠱ࠦẆ"))
                return None
            orchestration_strategy = None
            orchestration_metadata = self.bstack111ll11l_opy_.bstack111lll1llll_opy_()
            if self.bstack111ll11l_opy_ is not None:
                orchestration_strategy = self.bstack111ll11l_opy_.bstack1l111ll1ll_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack11111_opy_ (u"ࠥࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡷࡹࡸࡡࡵࡧࡪࡽࠥ࡯ࡳࠡࡐࡲࡲࡪ࠴ࠠࡄࡣࡱࡲࡴࡺࠠࡱࡴࡲࡧࡪ࡫ࡤࠡࡹ࡬ࡸ࡭ࠦࡴࡦࡵࡷࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠳ࠨẇ"))
                return None
            self.logger.info(bstack11111_opy_ (u"ࠦࡗ࡫࡯ࡳࡦࡨࡶ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡽࡩࡵࡪࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡷࡹࡸࡡࡵࡧࡪࡽ࠿ࠦࡻࡾࠤẈ").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack11111_opy_ (u"࡛ࠧࡳࡪࡰࡪࠤࡈࡒࡉࠡࡨ࡯ࡳࡼࠦࡦࡰࡴࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴ࠮ࠣẉ"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy, json.dumps(orchestration_metadata))
            else:
                self.logger.debug(bstack11111_opy_ (u"ࠨࡕࡴ࡫ࡱ࡫ࠥࡹࡤ࡬ࠢࡩࡰࡴࡽࠠࡧࡱࡵࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠯ࠤẊ"))
                self.bstack1111l1111ll_opy_.bstack11lll111l11_opy_(test_files, orchestration_strategy, orchestration_metadata)
                ordered_test_files = self.bstack1111l1111ll_opy_.bstack11ll1lll11l_opy_()
            if not ordered_test_files:
                return None
            self.bstack111l1l1l_opy_(bstack11111_opy_ (u"ࠢࡶࡲ࡯ࡳࡦࡪࡥࡥࡖࡨࡷࡹࡌࡩ࡭ࡧࡶࡇࡴࡻ࡮ࡵࠤẋ"), len(test_files))
            self.bstack111l1l1l_opy_(bstack11111_opy_ (u"ࠣࡰࡲࡨࡪࡏ࡮ࡥࡧࡻࠦẌ"), int(os.environ.get(bstack11111_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡐࡒࡈࡊࡥࡉࡏࡆࡈ࡜ࠧẍ")) or bstack11111_opy_ (u"ࠥ࠴ࠧẎ")))
            self.bstack111l1l1l_opy_(bstack11111_opy_ (u"ࠦࡹࡵࡴࡢ࡮ࡑࡳࡩ࡫ࡳࠣẏ"), int(os.environ.get(bstack11111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡓࡕࡄࡆࡡࡆࡓ࡚ࡔࡔࠣẐ")) or bstack11111_opy_ (u"ࠨ࠱ࠣẑ")))
            self.bstack111l1l1l_opy_(bstack11111_opy_ (u"ࠢࡥࡱࡺࡲࡱࡵࡡࡥࡧࡧࡘࡪࡹࡴࡇ࡫࡯ࡩࡸࡉ࡯ࡶࡰࡷࠦẒ"), len(ordered_test_files))
            self.bstack111l1l1l_opy_(bstack11111_opy_ (u"ࠣࡵࡳࡰ࡮ࡺࡔࡦࡵࡷࡷࡆࡖࡉࡄࡣ࡯ࡰࡈࡵࡵ࡯ࡶࠥẓ"), self.bstack1111l1111ll_opy_.bstack11lll111ll1_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack11111_opy_ (u"ࠤ࡞ࡶࡪࡵࡲࡥࡧࡵࡣࡹ࡫ࡳࡵࡡࡩ࡭ࡱ࡫ࡳ࡞ࠢࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡴࡸࡤࡦࡴ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡲࡡࡴࡵࡨࡷ࠿ࠦࡻࡾࠤẔ").format(e))
        return None
    def bstack111l1l1l_opy_(self, key, value):
        self.bstack1111l111l11_opy_[key] = value
    def bstack1l111l11l_opy_(self):
        return self.bstack1111l111l11_opy_