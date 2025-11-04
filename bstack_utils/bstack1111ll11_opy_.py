# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
import os
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack11ll1l1l111_opy_ import bstack11ll1l1111l_opy_
from bstack_utils.bstack1llllll11_opy_ import bstack1lllllll1_opy_
from bstack_utils.helper import bstack1ll11lll11_opy_
import json
class bstack1lll1ll11_opy_:
    _1ll1l1l1ll1_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack11111ll11ll_opy_ = bstack11ll1l1111l_opy_(self.config, logger)
        self.bstack1llllll11_opy_ = bstack1lllllll1_opy_.bstack1llllllll_opy_(config=self.config)
        self.bstack11111l1llll_opy_ = {}
        self.bstack111111ll_opy_ = False
        self.bstack11111lll111_opy_ = (
            self.__11111ll1ll1_opy_()
            and self.bstack1llllll11_opy_ is not None
            and self.bstack1llllll11_opy_.bstack1111lll1_opy_()
            and config.get(bstack11l1111_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨớ"), None) is not None
            and config.get(bstack11l1111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧỜ"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack1llllllll_opy_(cls, config, logger):
        if cls._1ll1l1l1ll1_opy_ is None and config is not None:
            cls._1ll1l1l1ll1_opy_ = bstack1lll1ll11_opy_(config, logger)
        return cls._1ll1l1l1ll1_opy_
    def bstack1111lll1_opy_(self):
        bstack11l1111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡇࡳࠥࡴ࡯ࡵࠢࡤࡴࡵࡲࡹࠡࡶࡨࡷࡹࠦ࡯ࡳࡦࡨࡶ࡮ࡴࡧࠡࡹ࡫ࡩࡳࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡕ࠱࠲ࡻࠣ࡭ࡸࠦ࡮ࡰࡶࠣࡩࡳࡧࡢ࡭ࡧࡧࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡒࡶࡩ࡫ࡲࡪࡰࡪࠤ࡮ࡹࠠ࡯ࡱࡷࠤࡪࡴࡡࡣ࡮ࡨࡨࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠡ࡫ࡶࠤࡓࡵ࡮ࡦࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠣ࡭ࡸࠦࡎࡰࡰࡨࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣờ")
        return self.bstack11111lll111_opy_ and self.bstack11111ll1l11_opy_()
    def bstack11111ll1l11_opy_(self):
        bstack11111ll1111_opy_ = os.getenv(bstack11l1111_opy_ (u"࠭ࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࡡࡘࡗࡊࡊࠧỞ"), self.config.get(bstack11l1111_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪở"), None))
        return bstack11111ll1111_opy_ in bstack11l11l1l1ll_opy_
    def __11111ll1ll1_opy_(self):
        bstack11ll11l1l11_opy_ = False
        for fw in bstack11l11ll11ll_opy_:
            if fw in self.config.get(bstack11l1111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫỠ"), bstack11l1111_opy_ (u"ࠩࠪỡ")):
                bstack11ll11l1l11_opy_ = True
        return bstack1ll11lll11_opy_(self.config.get(bstack11l1111_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧỢ"), bstack11ll11l1l11_opy_))
    def bstack11111ll1lll_opy_(self):
        return (not self.bstack1111lll1_opy_() and
                self.bstack1llllll11_opy_ is not None and self.bstack1llllll11_opy_.bstack1111lll1_opy_())
    def bstack11111ll111l_opy_(self):
        if not self.bstack11111ll1lll_opy_():
            return
        if self.config.get(bstack11l1111_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩợ"), None) is None or self.config.get(bstack11l1111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨỤ"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack11l1111_opy_ (u"ࠨࡔࡦࡵࡷࠤࡗ࡫࡯ࡳࡦࡨࡶ࡮ࡴࡧࠡࡥࡤࡲࠬࡺࠠࡸࡱࡵ࡯ࠥࡧࡳࠡࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠤࡴࡸࠠࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠥ࡯ࡳࠡࡰࡸࡰࡱ࠴ࠠࡑ࡮ࡨࡥࡸ࡫ࠠࡴࡧࡷࠤࡦࠦ࡮ࡰࡰ࠰ࡲࡺࡲ࡬ࠡࡸࡤࡰࡺ࡫࠮ࠣụ"))
        if not self.__11111ll1ll1_opy_():
            self.logger.info(bstack11l1111_opy_ (u"ࠢࡕࡧࡶࡸࠥࡘࡥࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡦࡥࡳ࠭ࡴࠡࡹࡲࡶࡰࠦࡡࡴࠢࡷࡩࡸࡺࡒࡦࡲࡲࡶࡹ࡯࡮ࡨࠢ࡬ࡷࠥࡪࡩࡴࡣࡥࡰࡪࡪ࠮ࠡࡒ࡯ࡩࡦࡹࡥࠡࡧࡱࡥࡧࡲࡥࠡ࡫ࡷࠤ࡫ࡸ࡯࡮ࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠥ࡬ࡩ࡭ࡧ࠱ࠦỦ"))
    def bstack11111ll11l1_opy_(self):
        return self.bstack111111ll_opy_
    def bstack111lll11_opy_(self, bstack11111ll1l1l_opy_):
        self.bstack111111ll_opy_ = bstack11111ll1l1l_opy_
        self.bstack1llll111l_opy_(bstack11l1111_opy_ (u"ࠣࡣࡳࡴࡱ࡯ࡥࡥࠤủ"), bstack11111ll1l1l_opy_)
    def bstack1lll11l1l_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack11l1111_opy_ (u"ࠤ࡞ࡶࡪࡵࡲࡥࡧࡵࡣࡹ࡫ࡳࡵࡡࡩ࡭ࡱ࡫ࡳ࡞ࠢࡑࡳࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴࠢࡳࡶࡴࡼࡩࡥࡧࡧࠤ࡫ࡵࡲࠡࡱࡵࡨࡪࡸࡩ࡯ࡩ࠱ࠦỨ"))
                return None
            orchestration_strategy = None
            orchestration_metadata = self.bstack1llllll11_opy_.bstack11l11111l1l_opy_()
            if self.bstack1llllll11_opy_ is not None:
                orchestration_strategy = self.bstack1llllll11_opy_.bstack1ll11ll1ll_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack11l1111_opy_ (u"ࠥࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡷࡹࡸࡡࡵࡧࡪࡽࠥ࡯ࡳࠡࡐࡲࡲࡪ࠴ࠠࡄࡣࡱࡲࡴࡺࠠࡱࡴࡲࡧࡪ࡫ࡤࠡࡹ࡬ࡸ࡭ࠦࡴࡦࡵࡷࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠳ࠨứ"))
                return None
            self.logger.info(bstack11l1111_opy_ (u"ࠦࡗ࡫࡯ࡳࡦࡨࡶ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡽࡩࡵࡪࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡷࡹࡸࡡࡵࡧࡪࡽ࠿ࠦࡻࡾࠤỪ").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack11l1111_opy_ (u"࡛ࠧࡳࡪࡰࡪࠤࡈࡒࡉࠡࡨ࡯ࡳࡼࠦࡦࡰࡴࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴ࠮ࠣừ"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy, json.dumps(orchestration_metadata))
            else:
                self.logger.debug(bstack11l1111_opy_ (u"ࠨࡕࡴ࡫ࡱ࡫ࠥࡹࡤ࡬ࠢࡩࡰࡴࡽࠠࡧࡱࡵࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠯ࠤỬ"))
                self.bstack11111ll11ll_opy_.bstack11ll1ll11l1_opy_(test_files, orchestration_strategy, orchestration_metadata)
                ordered_test_files = self.bstack11111ll11ll_opy_.bstack11ll1ll11ll_opy_()
            if not ordered_test_files:
                return None
            self.bstack1llll111l_opy_(bstack11l1111_opy_ (u"ࠢࡶࡲ࡯ࡳࡦࡪࡥࡥࡖࡨࡷࡹࡌࡩ࡭ࡧࡶࡇࡴࡻ࡮ࡵࠤử"), len(test_files))
            self.bstack1llll111l_opy_(bstack11l1111_opy_ (u"ࠣࡰࡲࡨࡪࡏ࡮ࡥࡧࡻࠦỮ"), int(os.environ.get(bstack11l1111_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡐࡒࡈࡊࡥࡉࡏࡆࡈ࡜ࠧữ")) or bstack11l1111_opy_ (u"ࠥ࠴ࠧỰ")))
            self.bstack1llll111l_opy_(bstack11l1111_opy_ (u"ࠦࡹࡵࡴࡢ࡮ࡑࡳࡩ࡫ࡳࠣự"), int(os.environ.get(bstack11l1111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡓࡕࡄࡆࡡࡆࡓ࡚ࡔࡔࠣỲ")) or bstack11l1111_opy_ (u"ࠨ࠱ࠣỳ")))
            self.bstack1llll111l_opy_(bstack11l1111_opy_ (u"ࠢࡥࡱࡺࡲࡱࡵࡡࡥࡧࡧࡘࡪࡹࡴࡇ࡫࡯ࡩࡸࡉ࡯ࡶࡰࡷࠦỴ"), len(ordered_test_files))
            self.bstack1llll111l_opy_(bstack11l1111_opy_ (u"ࠣࡵࡳࡰ࡮ࡺࡔࡦࡵࡷࡷࡆࡖࡉࡄࡣ࡯ࡰࡈࡵࡵ࡯ࡶࠥỵ"), self.bstack11111ll11ll_opy_.bstack11ll1l11lll_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack11l1111_opy_ (u"ࠤ࡞ࡶࡪࡵࡲࡥࡧࡵࡣࡹ࡫ࡳࡵࡡࡩ࡭ࡱ࡫ࡳ࡞ࠢࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡴࡸࡤࡦࡴ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡲࡡࡴࡵࡨࡷ࠿ࠦࡻࡾࠤỶ").format(e))
        return None
    def bstack1llll111l_opy_(self, key, value):
        self.bstack11111l1llll_opy_[key] = value
    def bstack111111l1ll_opy_(self):
        return self.bstack11111l1llll_opy_