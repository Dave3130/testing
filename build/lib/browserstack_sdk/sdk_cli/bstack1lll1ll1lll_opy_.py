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
import json
import time
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import (
    bstack1llll1ll1l1_opy_,
    bstack1lllll1ll1l_opy_,
    bstack1lllll11l1l_opy_,
    bstack1lll1l111l1_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1l1ll1l_opy_, bstack11l1llll1l_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1ll1_opy_ import bstack1lllll1l1l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_, bstack1llll1111l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll11ll1l1_opy_ import bstack1lll1l1l1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1lll11l_opy_ import bstack1lll11lllll_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack1l1lll11l1_opy_ import bstack11l1l1l11_opy_, bstack1ll1111111_opy_, bstack111l1l1lll_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1lll1l11l1l_opy_(bstack1lll11lllll_opy_):
    bstack1lll1lll111_opy_ = bstack11ll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡤࡳ࡫ࡹࡩࡷࡹࠢᄦ")
    bstack1lll1l1llll_opy_ = bstack11ll_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࠣᄧ")
    bstack1lll1l11l11_opy_ = bstack11ll_opy_ (u"ࠥࡲࡴࡴ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧᄨ")
    bstack1lll1l111ll_opy_ = bstack11ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦᄩ")
    bstack1lll11ll1ll_opy_ = bstack11ll_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡣࡷ࡫ࡦࡴࠤᄪ")
    bstack1lll1l1l11l_opy_ = bstack11ll_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡨࡸࡥࡢࡶࡨࡨࠧᄫ")
    bstack1lll1l1l111_opy_ = bstack11ll_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡴࡡ࡮ࡧࠥᄬ")
    bstack1lll11l1ll1_opy_ = bstack11ll_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡳࡵࡣࡷࡹࡸࠨᄭ")
    def __init__(self):
        super().__init__(bstack1lll11ll111_opy_=self.bstack1lll1lll111_opy_, frameworks=[bstack1lllll1l1l1_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1lllll1l1ll_opy_((bstack1lll1l1ll11_opy_.BEFORE_EACH, bstack1lll1ll111l_opy_.POST), self.bstack1lll1ll11l1_opy_)
        if bstack11l1llll1l_opy_():
            TestFramework.bstack1lllll1l1ll_opy_((bstack1lll1l1ll11_opy_.TEST, bstack1lll1ll111l_opy_.POST), self.bstack1lll1lll1l1_opy_)
        else:
            TestFramework.bstack1lllll1l1ll_opy_((bstack1lll1l1ll11_opy_.TEST, bstack1lll1ll111l_opy_.PRE), self.bstack1lll1lll1l1_opy_)
        TestFramework.bstack1lllll1l1ll_opy_((bstack1lll1l1ll11_opy_.TEST, bstack1lll1ll111l_opy_.POST), self.bstack1lll1l11lll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1ll11l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111l1_opy_,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        bstack1llll1111ll_opy_ = self.bstack1llll111ll1_opy_(instance.context)
        if not bstack1llll1111ll_opy_:
            self.logger.debug(bstack11ll_opy_ (u"ࠤࡶࡩࡹࡥࡡࡤࡶ࡬ࡺࡪࡥࡰࡢࡩࡨ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢᄮ") + str(bstack1lllll1l11l_opy_) + bstack11ll_opy_ (u"ࠥࠦᄯ"))
            return
        f.bstack1llllll1lll_opy_(instance, bstack1lll1l11l1l_opy_.bstack1lll1l1llll_opy_, bstack1llll1111ll_opy_)
    def bstack1llll111ll1_opy_(self, context: bstack1lll1l111l1_opy_, bstack1llll11111l_opy_= True):
        if bstack1llll11111l_opy_:
            bstack1llll1111ll_opy_ = self.bstack1lll1llllll_opy_(context, reverse=True)
        else:
            bstack1llll1111ll_opy_ = self.bstack1lll11lll11_opy_(context, reverse=True)
        return [f for f in bstack1llll1111ll_opy_ if f[1].state != bstack1llll1ll1l1_opy_.QUIT]
    def bstack1lll1lll1l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111l1_opy_,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1ll11l1_opy_(f, instance, bstack1lllll1l11l_opy_, *args, **kwargs)
        if not bstack1lll1l1ll1l_opy_:
            self.logger.debug(bstack11ll_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄰ") + str(kwargs) + bstack11ll_opy_ (u"ࠧࠨᄱ"))
            return
        bstack1llll1111ll_opy_ = f.get_state(instance, bstack1lll1l11l1l_opy_.bstack1lll1l1llll_opy_, [])
        if not bstack1llll1111ll_opy_:
            self.logger.debug(bstack11ll_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᄲ") + str(kwargs) + bstack11ll_opy_ (u"ࠢࠣᄳ"))
            return
        if len(bstack1llll1111ll_opy_) > 1:
            self.logger.debug(
                bstack11l1llll_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡲࡤ࡫ࡪࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥᄴ"))
        bstack1lll1ll1l1l_opy_, bstack1lll1l1lll1_opy_ = bstack1llll1111ll_opy_[0]
        page = bstack1lll1ll1l1l_opy_()
        if not page:
            self.logger.debug(bstack11ll_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᄵ") + str(kwargs) + bstack11ll_opy_ (u"ࠥࠦᄶ"))
            return
        bstack111l111l1l_opy_ = getattr(args[0], bstack11ll_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦᄷ"), None)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11ll_opy_ (u"ࠧࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠥᄸ")).get(bstack11ll_opy_ (u"ࠨࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣᄹ")):
            try:
                page.evaluate(bstack11ll_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣᄺ"),
                            bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠬᄻ") + json.dumps(
                                bstack111l111l1l_opy_) + bstack11ll_opy_ (u"ࠤࢀࢁࠧᄼ"))
            except Exception as e:
                self.logger.debug(bstack11ll_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥࢁࡽࠣᄽ"), e)
    def bstack1lll1l11lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111l1_opy_,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1ll11l1_opy_(f, instance, bstack1lllll1l11l_opy_, *args, **kwargs)
        if not bstack1lll1l1ll1l_opy_:
            self.logger.debug(bstack11ll_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄾ") + str(kwargs) + bstack11ll_opy_ (u"ࠧࠨᄿ"))
            return
        bstack1llll1111ll_opy_ = f.get_state(instance, bstack1lll1l11l1l_opy_.bstack1lll1l1llll_opy_, [])
        if not bstack1llll1111ll_opy_:
            self.logger.debug(bstack11ll_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᅀ") + str(kwargs) + bstack11ll_opy_ (u"ࠢࠣᅁ"))
            return
        if len(bstack1llll1111ll_opy_) > 1:
            self.logger.debug(
                bstack11l1llll_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡲࡤ࡫ࡪࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥᅂ"))
        bstack1lll1ll1l1l_opy_, bstack1lll1l1lll1_opy_ = bstack1llll1111ll_opy_[0]
        page = bstack1lll1ll1l1l_opy_()
        if not page:
            self.logger.debug(bstack11ll_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᅃ") + str(kwargs) + bstack11ll_opy_ (u"ࠥࠦᅄ"))
            return
        status = f.get_state(instance, TestFramework.bstack1lll11ll11l_opy_, None)
        if not status:
            self.logger.debug(bstack11ll_opy_ (u"ࠦࡳࡵࠠࡴࡶࡤࡸࡺࡹࠠࡧࡱࡵࠤࡹ࡫ࡳࡵ࠮ࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢᅅ") + str(bstack1lllll1l11l_opy_) + bstack11ll_opy_ (u"ࠧࠨᅆ"))
            return
        bstack1llll111l1l_opy_ = {bstack11ll_opy_ (u"ࠨࡳࡵࡣࡷࡹࡸࠨᅇ"): status.lower()}
        bstack1lll1ll1111_opy_ = f.get_state(instance, TestFramework.bstack1lll1l1111l_opy_, None)
        if status.lower() == bstack11ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᅈ") and bstack1lll1ll1111_opy_ is not None:
            bstack1llll111l1l_opy_[bstack11ll_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨᅉ")] = bstack1lll1ll1111_opy_[0][bstack11ll_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬᅊ")][0] if isinstance(bstack1lll1ll1111_opy_, list) else str(bstack1lll1ll1111_opy_)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11ll_opy_ (u"ࠥࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠣᅋ")).get(bstack11ll_opy_ (u"ࠦࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣᅌ")):
            try:
                page.evaluate(
                        bstack11ll_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨᅍ"),
                        bstack11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࠫᅎ")
                        + json.dumps(bstack1llll111l1l_opy_)
                        + bstack11ll_opy_ (u"ࠢࡾࠤᅏ")
                    )
            except Exception as e:
                self.logger.debug(bstack11ll_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥࢁࡽࠣᅐ"), e)
    def bstack1lll1llll11_opy_(
        self,
        instance: bstack1llll1111l1_opy_,
        f: TestFramework,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1ll11l1_opy_(f, instance, bstack1lllll1l11l_opy_, *args, **kwargs)
        if not bstack1lll1l1ll1l_opy_:
            self.logger.debug(
                bstack11l1llll_opy_ (u"ࠤࡰࡥࡷࡱ࡟ࡰ࠳࠴ࡽࡤࡹࡹ࡯ࡥ࠽ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥᅑ"))
            return
        bstack1llll1111ll_opy_ = f.get_state(instance, bstack1lll1l11l1l_opy_.bstack1lll1l1llll_opy_, [])
        if not bstack1llll1111ll_opy_:
            self.logger.debug(bstack11ll_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᅒ") + str(kwargs) + bstack11ll_opy_ (u"ࠦࠧᅓ"))
            return
        if len(bstack1llll1111ll_opy_) > 1:
            self.logger.debug(
                bstack11l1llll_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠࡼ࡮ࡨࡲ࠭ࡶࡡࡨࡧࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࢁ࡫ࡸࡣࡵ࡫ࡸࢃࠢᅔ"))
        bstack1lll1ll1l1l_opy_, bstack1lll1l1lll1_opy_ = bstack1llll1111ll_opy_[0]
        page = bstack1lll1ll1l1l_opy_()
        if not page:
            self.logger.debug(bstack11ll_opy_ (u"ࠨ࡭ࡢࡴ࡮ࡣࡴ࠷࠱ࡺࡡࡶࡽࡳࡩ࠺ࠡࡰࡲࠤࡵࡧࡧࡦࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᅕ") + str(kwargs) + bstack11ll_opy_ (u"ࠢࠣᅖ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack11ll_opy_ (u"ࠣࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࡔࡻࡱࡧ࠿ࠨᅗ") + str(timestamp)
        try:
            page.evaluate(
                bstack11ll_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥᅘ"),
                bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨᅙ").format(
                    json.dumps(
                        {
                            bstack11ll_opy_ (u"ࠦࡦࡩࡴࡪࡱࡱࠦᅚ"): bstack11ll_opy_ (u"ࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢᅛ"),
                            bstack11ll_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤᅜ"): {
                                bstack11ll_opy_ (u"ࠢࡵࡻࡳࡩࠧᅝ"): bstack11ll_opy_ (u"ࠣࡃࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠧᅞ"),
                                bstack11ll_opy_ (u"ࠤࡧࡥࡹࡧࠢᅟ"): data,
                                bstack11ll_opy_ (u"ࠥࡰࡪࡼࡥ࡭ࠤᅠ"): bstack11ll_opy_ (u"ࠦࡩ࡫ࡢࡶࡩࠥᅡ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack11ll_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡱ࠴࠵ࡾࠦࡡ࡯ࡰࡲࡸࡦࡺࡩࡰࡰࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࢀࢃࠢᅢ"), e)
    def bstack1lll1llll1l_opy_(
        self,
        instance: bstack1llll1111l1_opy_,
        f: TestFramework,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1ll11l1_opy_(f, instance, bstack1lllll1l11l_opy_, *args, **kwargs)
        if f.get_state(instance, bstack1lll1l11l1l_opy_.bstack1lll1l1l11l_opy_, False):
            return
        self.bstack1lllll111ll_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll1l111l_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1lllll1_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l11111_opy_)
        req.test_framework_state = bstack1lllll1l11l_opy_[0].name
        req.test_hook_state = bstack1lllll1l11l_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1llll111l11_opy_)
        for bstack1lll1ll1l11_opy_ in bstack1lll1l1l1l1_opy_.bstack1lll1l11ll1_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack11ll_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠧᅣ")
                if bstack1lll1l1ll1l_opy_
                else bstack11ll_opy_ (u"ࠢࡶࡰ࡮ࡲࡴࡽ࡮ࡠࡩࡵ࡭ࡩࠨᅤ")
            )
            session.ref = bstack1lll1ll1l11_opy_.ref()
            session.hub_url = bstack1lll1l1l1l1_opy_.get_state(bstack1lll1ll1l11_opy_, bstack1lll1l1l1l1_opy_.bstack1lll11lll1l_opy_, bstack11ll_opy_ (u"ࠣࠤᅥ"))
            session.framework_name = bstack1lll1ll1l11_opy_.framework_name
            session.framework_version = bstack1lll1ll1l11_opy_.framework_version
            session.framework_session_id = bstack1lll1l1l1l1_opy_.get_state(bstack1lll1ll1l11_opy_, bstack1lll1l1l1l1_opy_.bstack1lll11llll1_opy_, bstack11ll_opy_ (u"ࠤࠥᅦ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1l1l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111l1_opy_,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs
    ):
        bstack1llll1111ll_opy_ = f.get_state(instance, bstack1lll1l11l1l_opy_.bstack1lll1l1llll_opy_, [])
        if not bstack1llll1111ll_opy_:
            self.logger.debug(bstack11ll_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᅧ") + str(kwargs) + bstack11ll_opy_ (u"ࠦࠧᅨ"))
            return
        if len(bstack1llll1111ll_opy_) > 1:
            self.logger.debug(bstack11ll_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠࡼ࡮ࡨࡲ࠭ࡶࡡࡨࡧࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᅩ") + str(kwargs) + bstack11ll_opy_ (u"ࠨࠢᅪ"))
        bstack1lll1ll1l1l_opy_, bstack1lll1l1lll1_opy_ = bstack1llll1111ll_opy_[0]
        page = bstack1lll1ll1l1l_opy_()
        if not page:
            self.logger.debug(bstack11ll_opy_ (u"ࠢࡨࡧࡷࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡱࡳࠥࡶࡡࡨࡧࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᅫ") + str(kwargs) + bstack11ll_opy_ (u"ࠣࠤᅬ"))
            return
        return page
    def bstack1lll1ll1ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111l1_opy_,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1llll111111_opy_ = {}
        for bstack1lll1ll1l11_opy_ in bstack1lll1l1l1l1_opy_.bstack1lll1l11ll1_opy_.values():
            caps = bstack1lll1l1l1l1_opy_.get_state(bstack1lll1ll1l11_opy_, bstack1lll1l1l1l1_opy_.bstack1lll1lll1ll_opy_, bstack11ll_opy_ (u"ࠤࠥᅭ"))
        bstack1llll111111_opy_[bstack11ll_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠣᅮ")] = caps.get(bstack11ll_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࠧᅯ"), bstack11ll_opy_ (u"ࠧࠨᅰ"))
        bstack1llll111111_opy_[bstack11ll_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧᅱ")] = caps.get(bstack11ll_opy_ (u"ࠢࡰࡵࠥᅲ"), bstack11ll_opy_ (u"ࠣࠤᅳ"))
        bstack1llll111111_opy_[bstack11ll_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦᅴ")] = caps.get(bstack11ll_opy_ (u"ࠥࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠢᅵ"), bstack11ll_opy_ (u"ࠦࠧᅶ"))
        bstack1llll111111_opy_[bstack11ll_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳࠨᅷ")] = caps.get(bstack11ll_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣᅸ"), bstack11ll_opy_ (u"ࠢࠣᅹ"))
        return bstack1llll111111_opy_
    def bstack1lll11l1lll_opy_(self, page: object, bstack1llll111lll_opy_, args={}):
        try:
            bstack1lll1ll11ll_opy_ = bstack11ll_opy_ (u"ࠣࠤࠥࠬ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࠨ࠯࠰࠱ࡦࡸࡺࡡࡤ࡭ࡖࡨࡰࡇࡲࡨࡵࠬࠤࢀࢁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡵࡩࡹࡻࡲ࡯ࠢࡱࡩࡼࠦࡐࡳࡱࡰ࡭ࡸ࡫ࠨࠩࡴࡨࡷࡴࡲࡶࡦ࠮ࠣࡶࡪࡰࡥࡤࡶࠬࠤࡂࡄࠠࡼࡽࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡥࡷࡹࡧࡣ࡬ࡕࡧ࡯ࡆࡸࡧࡴ࠰ࡳࡹࡸ࡮ࠨࡳࡧࡶࡳࡱࡼࡥࠪ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡾࡪࡳࡥࡢࡰࡦࡼࢁࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾࡿࠬ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࢂ࠯ࠨࡼࡣࡵ࡫ࡤࡰࡳࡰࡰࢀ࠭ࠧࠨࠢᅺ")
            bstack1llll111lll_opy_ = bstack1llll111lll_opy_.replace(bstack11ll_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧᅻ"), bstack11ll_opy_ (u"ࠥࡦࡸࡺࡡࡤ࡭ࡖࡨࡰࡇࡲࡨࡵࠥᅼ"))
            script = bstack1lll1ll11ll_opy_.format(fn_body=bstack1llll111lll_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack11ll_opy_ (u"ࠦࡦ࠷࠱ࡺࡡࡶࡧࡷ࡯ࡰࡵࡡࡨࡼࡪࡩࡵࡵࡧ࠽ࠤࡊࡸࡲࡰࡴࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡥ࠶࠷ࡹࠡࡵࡦࡶ࡮ࡶࡴ࠭ࠢࠥᅽ") + str(e) + bstack11ll_opy_ (u"ࠧࠨᅾ"))