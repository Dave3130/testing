# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11l1ll11l1l_opy_
from browserstack_sdk.bstack11111ll1_opy_ import bstack111111ll_opy_
def _11l1ll111ll_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack11l1l1ll1ll_opy_:
    def __init__(self, handler):
        self._11l1ll11ll1_opy_ = {}
        self._11l1ll11lll_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack111111ll_opy_.version()
        if bstack11l1ll11l1l_opy_(pytest_version, bstack1l1_opy_ (u"ࠤ࠻࠲࠶࠴࠱ࠣឍ")) >= 0:
            self._11l1ll11ll1_opy_[bstack1l1_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ណ")] = Module._register_setup_function_fixture
            self._11l1ll11ll1_opy_[bstack1l1_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬត")] = Module._register_setup_module_fixture
            self._11l1ll11ll1_opy_[bstack1l1_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠬថ")] = Class._register_setup_class_fixture
            self._11l1ll11ll1_opy_[bstack1l1_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠧទ")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack11l1ll1111l_opy_(bstack1l1_opy_ (u"ࠧࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪធ"))
            Module._register_setup_module_fixture = self.bstack11l1ll1111l_opy_(bstack1l1_opy_ (u"ࠨ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩន"))
            Class._register_setup_class_fixture = self.bstack11l1ll1111l_opy_(bstack1l1_opy_ (u"ࠩࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠩប"))
            Class._register_setup_method_fixture = self.bstack11l1ll1111l_opy_(bstack1l1_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࠫផ"))
        else:
            self._11l1ll11ll1_opy_[bstack1l1_opy_ (u"ࠫ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧព")] = Module._inject_setup_function_fixture
            self._11l1ll11ll1_opy_[bstack1l1_opy_ (u"ࠬࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ភ")] = Module._inject_setup_module_fixture
            self._11l1ll11ll1_opy_[bstack1l1_opy_ (u"࠭ࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ម")] = Class._inject_setup_class_fixture
            self._11l1ll11ll1_opy_[bstack1l1_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨយ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack11l1ll1111l_opy_(bstack1l1_opy_ (u"ࠨࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫរ"))
            Module._inject_setup_module_fixture = self.bstack11l1ll1111l_opy_(bstack1l1_opy_ (u"ࠩࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪល"))
            Class._inject_setup_class_fixture = self.bstack11l1ll1111l_opy_(bstack1l1_opy_ (u"ࠪࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠪវ"))
            Class._inject_setup_method_fixture = self.bstack11l1ll1111l_opy_(bstack1l1_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠬឝ"))
    def bstack11l1l1llll1_opy_(self, bstack11l1l1lll11_opy_, hook_type):
        bstack11l1l1lllll_opy_ = id(bstack11l1l1lll11_opy_.__class__)
        if (bstack11l1l1lllll_opy_, hook_type) in self._11l1ll11lll_opy_:
            return
        meth = getattr(bstack11l1l1lll11_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._11l1ll11lll_opy_[(bstack11l1l1lllll_opy_, hook_type)] = meth
            setattr(bstack11l1l1lll11_opy_, hook_type, self.bstack11l1l1lll1l_opy_(hook_type, bstack11l1l1lllll_opy_))
    def bstack11l1ll111l1_opy_(self, instance, bstack11l1l1ll111_opy_):
        if bstack11l1l1ll111_opy_ == bstack1l1_opy_ (u"ࠧ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣឞ"):
            self.bstack11l1l1llll1_opy_(instance.obj, bstack1l1_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠢស"))
            self.bstack11l1l1llll1_opy_(instance.obj, bstack1l1_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࠦហ"))
        if bstack11l1l1ll111_opy_ == bstack1l1_opy_ (u"ࠣ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠤឡ"):
            self.bstack11l1l1llll1_opy_(instance.obj, bstack1l1_opy_ (u"ࠤࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠣអ"))
            self.bstack11l1l1llll1_opy_(instance.obj, bstack1l1_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠧឣ"))
        if bstack11l1l1ll111_opy_ == bstack1l1_opy_ (u"ࠦࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠦឤ"):
            self.bstack11l1l1llll1_opy_(instance.obj, bstack1l1_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣࡨࡲࡡࡴࡵࠥឥ"))
            self.bstack11l1l1llll1_opy_(instance.obj, bstack1l1_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡥ࡯ࡥࡸࡹࠢឦ"))
        if bstack11l1l1ll111_opy_ == bstack1l1_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣឧ"):
            self.bstack11l1l1llll1_opy_(instance.obj, bstack1l1_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠢឨ"))
            self.bstack11l1l1llll1_opy_(instance.obj, bstack1l1_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠦឩ"))
    @staticmethod
    def bstack11l1l1ll11l_opy_(hook_type, func, args):
        if hook_type in [bstack1l1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠩឪ"), bstack1l1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ឫ")]:
            _11l1ll111ll_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack11l1l1lll1l_opy_(self, hook_type, bstack11l1l1lllll_opy_):
        def bstack11l1l1ll1l1_opy_(arg=None):
            self.handler(hook_type, bstack1l1_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬឬ"))
            result = None
            try:
                bstack1l11111111l_opy_ = self._11l1ll11lll_opy_[(bstack11l1l1lllll_opy_, hook_type)]
                self.bstack11l1l1ll11l_opy_(hook_type, bstack1l11111111l_opy_, (arg,))
                result = Result(result=bstack1l1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ឭ"))
            except Exception as e:
                result = Result(result=bstack1l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧឮ"), exception=e)
                self.handler(hook_type, bstack1l1_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧឯ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1l1_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࠨឰ"), result)
        def bstack11l1ll11111_opy_(this, arg=None):
            self.handler(hook_type, bstack1l1_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪឱ"))
            result = None
            exception = None
            try:
                self.bstack11l1l1ll11l_opy_(hook_type, self._11l1ll11lll_opy_[hook_type], (this, arg))
                result = Result(result=bstack1l1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫឲ"))
            except Exception as e:
                result = Result(result=bstack1l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬឳ"), exception=e)
                self.handler(hook_type, bstack1l1_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬ឴"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1l1_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭឵"), result)
        if hook_type in [bstack1l1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧា"), bstack1l1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠫិ")]:
            return bstack11l1ll11111_opy_
        return bstack11l1l1ll1l1_opy_
    def bstack11l1ll1111l_opy_(self, bstack11l1l1ll111_opy_):
        def bstack11l1ll11l11_opy_(this, *args, **kwargs):
            self.bstack11l1ll111l1_opy_(this, bstack11l1l1ll111_opy_)
            self._11l1ll11ll1_opy_[bstack11l1l1ll111_opy_](this, *args, **kwargs)
        return bstack11l1ll11l11_opy_